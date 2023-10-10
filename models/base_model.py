#!/usr/bin/python3
"""Define BaseModel class"""
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

        obj_dict = {
                "__class__": class_name,
                "id": self.id,
                "created_at": iso_created_at,
                "updated_at": iso_updated_at,
                }
        return obj_dict

    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
