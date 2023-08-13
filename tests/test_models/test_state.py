#!/usr/bin/python3

"""Module to test the State
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class Test State
    """

    def test_state(self):
        """Function to test State
        """
        my_model = State()
        my_model.name = "My State"

        self.assertTrue(hasattr(my_model, "name"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

        my_model_json = my_model.to_dict()

        self.assertTrue(hasattr(my_model_json, "__class__"))

        my_new_model = State(**my_model_json)

        self.assertTrue(hasattr(my_new_model, "name"))
        self.assertTrue(hasattr(my_new_model, "id"))
        self.assertTrue(hasattr(my_new_model, "created_at"))
        self.assertTrue(hasattr(my_new_model, "updated_at"))
        self.assertFalse(my_new_model is my_model)


if __name__ == '__main__':
    unittest.main()
