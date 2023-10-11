#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ a class Amenity that inherits from BaseModel"""

    @method
    def __init__(self):
        super().__init__()

        """public class attributes"""
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = ""
        self.number_bathrooms = ""
        self.max_guest = ""
        self.price_by_night = ""
        self.latitude = ""
        self.longitude = ""
        self.amenity_ids = ""

    def __str__(self):
        # Custom __str__ method to print Amenity object information
        return "[Amenity ({}) {}".format(self.id, self.__dict__)
