#!/usr/bin/python3

"""Module to test the Base model
"""
import unittest
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):
    """Class Test Base
    """

    def test_base_model(self):
        """Function to test base model
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertTrue(hasattr(my_model, "name"))
        self.assertTrue(hasattr(my_model, "my_number"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

        my_model_json = my_model.to_dict()

        self.assertTrue(hasattr(my_model_json, "__class__"))

        my_new_model = BaseModel(**my_model_json)

        self.assertTrue(hasattr(my_new_model, "name"))
        self.assertTrue(hasattr(my_new_model, "my_number"))
        self.assertTrue(hasattr(my_new_model, "id"))
        self.assertTrue(hasattr(my_new_model, "created_at"))
        self.assertTrue(hasattr(my_new_model, "updated_at"))
        self.assertFalse(my_new_model is my_model)


if __name__ == '__main__':
    unittest.main()
