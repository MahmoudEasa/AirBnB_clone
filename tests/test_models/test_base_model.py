#!/usr/bin/python3

"""Module to test the Base model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class Test Base Model
    """

    def setUp(self):
        """Set up for the tests"""
        self.bm = BaseModel()

    def test_attributes(self):
        """Function to test base model
        """
        self.bm.name = "My First Model"
        self.bm.my_number = 89

        self.assertTrue(hasattr(self.bm, "name"))
        self.assertTrue(hasattr(self.bm, "my_number"))
        self.assertTrue(hasattr(self.bm, "id"))
        self.assertTrue(hasattr(self.bm, "created_at"))
        self.assertTrue(hasattr(self.bm, "updated_at"))
        self.assertTrue(self.bm.name == "My First Model")
        self.assertTrue(self.bm.my_number == 89)
        self.assertEqual(type(self.bm.name), str)
        self.assertEqual(type(self.bm.my_number), int)
        self.assertEqual(type(self.bm.id), str)
        self.assertEqual(type(self.bm.created_at), datetime)
        self.assertEqual(type(self.bm.updated_at), datetime)

        my_model_json = self.bm.to_dict()

        self.assertTrue(hasattr(my_model_json, "__class__"))

        my_new_model = BaseModel(**my_model_json)

        self.assertTrue(hasattr(my_new_model, "name"))
        self.assertTrue(hasattr(my_new_model, "my_number"))
        self.assertTrue(hasattr(my_new_model, "id"))
        self.assertTrue(hasattr(my_new_model, "created_at"))
        self.assertTrue(hasattr(my_new_model, "updated_at"))
        self.assertTrue(my_new_model.name == "My First Model")
        self.assertTrue(my_new_model.my_number == 89)
        self.assertFalse(my_new_model is self.bm)


if __name__ == '__main__':
    unittest.main()
