#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    """ a class Place that inherits from BaseModel"""

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
        # Custom __str__ method to print Place object information
        return "[Place ({}) {}".format(self.id, self.__dict__)
