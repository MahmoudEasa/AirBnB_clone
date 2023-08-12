#!/usr/bin/python3

"""Model to Write a class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City

        Attributes:
            state_id (str): The State.id
            name (str): The Name
    """

    state_id = ""
    name = ""
