#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """ a class City that inherits from BaseModel"""

    @method
    def __init__(self):
        super().__init__()

        """public class attributes"""
        self.state_id = ""
        self.name = ""

    def __str__(self):
        # Custom __str__ method to print City object information
        return "[City ({}) {}".format(self.id, self.__dict__)
