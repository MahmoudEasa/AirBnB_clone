#!/usr/bin/python3

"""Model to Write a class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review

        Attributes:
            place_id (str): The Place.id
            user_id (str): The User.id
            text (str): The Text
    """

    place_id = ""
    user_id = ""
    text = ""
