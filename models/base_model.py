#!/usr/bin/python3
"""Defines BaseModel class"""
import uuid
import datetime
import models


class BaseModel:
    """
    A base class that defines all common attributes/methods
    for other child classes.

    Attributes:
        id (str): Unique id for an instance created
        created_at (datetime): Current time when an instance is created
        updated_at (datetime): Current time when an instance is
        created or updated
    Methods:
        save(self): Updates the public instance attribute
            updated_at with the current datetime and saves to storage
        to_dict(self): Returns a dictionary containing all
            keys/values of __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiates the class
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.datetime.now()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime and saves to storage
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        class_name = self.__class__.__name__
        iso_created_at = self.created_at.isoformat()
        iso_updated_at = self.updated_at.isoformat()

        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = iso_created_at
        obj_dict["updated_at"] = iso_updated_at
        obj_dict["__class__"] = class_name
        return obj_dict

    def __str__(self):
        """Generates a string representation of the BaseModel class"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.to_dict()}"
