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
        id: (string) unique id for an instance created
        created_at: (datetime) current time when an instance is created
        updated_at: (datetime) current time when an instance is
        created or updated
    Methods:
        save(self): updates the public instance attribute
            updated_at with current datetiime
        to_dict(self): returns a dictionary containing all
            keys/values of __dict__ of the instance
    """
    def __init__(self, *args, **kwargs):
        """instantiates the class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            """ """
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            if 'created_at' in kwargs:
                self.created_at = datetime.datetime.strptime(kwargs['created_at'],
                                                             '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
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
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
