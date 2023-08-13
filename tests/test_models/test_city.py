#!/usr/bin/python3

"""Module to test the city
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class Test City
    """

    def test_city(self):
        """Function to test city
        """
        my_model = City()
        my_model.name = "My City"
        my_model.state_id = 89

        self.assertTrue(hasattr(my_model, "name"))
        self.assertTrue(hasattr(my_model, "state_id"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

        my_model_json = my_model.to_dict()

        self.assertTrue(hasattr(my_model_json, "__class__"))

        my_new_model = City(**my_model_json)

        self.assertTrue(hasattr(my_new_model, "name"))
        self.assertTrue(hasattr(my_new_model, "state_id"))
        self.assertTrue(hasattr(my_new_model, "id"))
        self.assertTrue(hasattr(my_new_model, "created_at"))
        self.assertTrue(hasattr(my_new_model, "updated_at"))
        self.assertFalse(my_new_model is my_model)


if __name__ == '__main__':
    unittest.main()
