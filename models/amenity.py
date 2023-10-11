#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ a class Amenity that inherits from BaseModel"""

    @method
    def __init__(self):
        super().__init__()

        """public class attributes"""
        self.name = ""

    def __str__(self):
        # Custom __str__ method to print Amenity object information
        return "[Amenity ({}) {}".format(self.id, self.__dict__)
