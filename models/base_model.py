#!/usr/bin/python3
<<<<<<< HEAD

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Generate a unique ID as a string
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()  # Create a copy of the instance's __dict__

        # Convert created_at and updated_at to ISO format strings
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        # Add the __class__ key with the class name
        obj_dict['__class__'] = self.__class__.__name__

        return obj_dict
=======
"""Defines BaseModel class"""
import uuid
import datetime

class BaseModel():
    """
    A base class that defines all common attributes/methods
    for other child classes.

    Attributes:
        id: (string) unique id for an instance created
        created_at: (datetime) current time when an instance is created
        updated_at: (datetime) current time when an instance is created or updated
    Methods:
        save(self): updates the public instance attribute
            updated_at with current datetiime
        to_dict(self): returns a dictionary containing all
            keys/values of __dict__ of the instance
    """

    def __init__(self):
        """Instatiates class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()

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
>>>>>>> main
