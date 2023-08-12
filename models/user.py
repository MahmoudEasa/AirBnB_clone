#!/usr/bin/python3

"""Model to Write a class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User

        Attributes:
            email (str): The Email
            password (str): The password
            first_name (str): The First Name
            last_name (str): The Last Name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
