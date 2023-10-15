#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ a class Amenity that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = ""
