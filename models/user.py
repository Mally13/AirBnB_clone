#!/usr/bin/python3

from models.base_model import BaseModel


@dataclass
class User(BaseModel):
    """ a class User that inherits from BaseModel"""

    @method
    def __init__(self):
        super().__init__()

        """pulblic class attributes"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        # Custom __str__ method to print User object information
        return "[User] ({}) {}".format(self.id, self.__dict__)
