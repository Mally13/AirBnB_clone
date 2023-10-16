#!/usr/bin/python3
"""Defines class FileStorage"""
import json
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.state import State


class FileStorage:
    """
    Class FileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances
    Attributes:
        __file_path: (string) - path to the JSON file (ex: file.json)
        __objects: (dictionary) - empty but will store all objects by
        <class name>.id (ex: to store a BaseModel object with id=12121212,
            the key will be BaseModel.12121212)
    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with ksey <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (only if the
        JSON file(__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictonary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        datadict = FileStorage.__objects
        objdict = {obj: datadict[obj].to_dict() for obj in datadict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as file:
                objdict = json.load(file)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
