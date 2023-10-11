#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """ a class Review that inherits from BaseModel"""

    @method
    def __init__(self):
        super().__init__()

        """public class attributes"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        # Custom __str__ method to print Review object information
        return "[Review ({}) {}".format(self.id, self.__dict__)
