#!/usr/bin/python3
"""Defines class FileStorage"""
import json

class FileStorage():
    """
    Class FileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances
    
    Attributes:
        __file_path: (string) - path to the JSON file (ex: file.json)
        __objects: (dictionary) - empty but will store all objects by <class name>.id
            (ex: to store a BaseModel object with id=12121212,
            the key will be BaseModel.12121212)

    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictonary objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dumb(data, file)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = eval(class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
