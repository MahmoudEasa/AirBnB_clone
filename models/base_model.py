#!/usr/bin/python3

"""Model for defining all common attributes/methods for other classes
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class Base Model"""

    def __init__(self, *args, **kwargs):
        """Function Init

            Args:
                *args: list of arguments
                **kwargs: dict of keys and values arguments
        """

        if kwargs:
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    val = datetime.fromisoformat(val)

                if key == "__class__":
                    continue

                self.__dict__[key] = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return: [<class name>] (<self.id>) <self.__dict__>
        """

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute updated_at
            with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all models/base_model.py
            keys/values of __dict__ of the instance
        """

        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__

        return (dict_copy)
