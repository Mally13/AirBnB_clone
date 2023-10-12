#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """ a class Review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
