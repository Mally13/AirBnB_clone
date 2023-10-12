#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """ a class State that inherits from BaseModel"""
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **args)
