#!/usr/bin/python3

"""Module to test the Amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class Test Amenity
    """

    def test_amenity(self):
        """Function to test amenity
        """
        my_model = Amenity()
        my_model.name = "My amenity"

        self.assertTrue(hasattr(my_model, "name"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

        my_model_json = my_model.to_dict()

        self.assertTrue(hasattr(my_model_json, "__class__"))

        my_new_model = Amenity(**my_model_json)

        self.assertTrue(hasattr(my_new_model, "name"))
        self.assertTrue(hasattr(my_new_model, "id"))
        self.assertTrue(hasattr(my_new_model, "created_at"))
        self.assertTrue(hasattr(my_new_model, "updated_at"))
        self.assertFalse(my_new_model is my_model)


if __name__ == '__main__':
    unittest.main()
