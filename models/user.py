#!/usr/bin/python3


class User:
    """ a class User that inherits from BaseModel"""

    @method
    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
