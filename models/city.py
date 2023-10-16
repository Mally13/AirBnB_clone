#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """ a class City that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """public class attributes"""

        self.state_id = ""
        self.name = ""
