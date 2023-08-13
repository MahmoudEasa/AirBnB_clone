#!/usr/bin/python3

"""Module to test the User
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class Test User
    """

    def test_user(self):
        """Function to test User
        """
        my_model = User()
        my_model.email = "user@email.com"
        my_model.password = "123"
        my_model.first_name = "user1"
        my_model.last_name = "user2"

        self.assertTrue(hasattr(my_model, "email"))
        self.assertTrue(hasattr(my_model, "password"))
        self.assertTrue(hasattr(my_model, "first_name"))
        self.assertTrue(hasattr(my_model, "last_name"))

        self.assertEqual(type(my_model.email), str)
        self.assertEqual(type(my_model.password), str)
        self.assertEqual(type(my_model.first_name), str)
        self.assertEqual(type(my_model.last_name), str)

        self.assertEqual(my_model.email, "user@email.com")
        self.assertEqual(my_model.password, "123")
        self.assertEqual(my_model.first_name, "user1")
        self.assertEqual(my_model.last_name, "user2")

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

        my_model_json = my_model.to_dict()

        self.assertTrue(hasattr(my_model_json, "__class__"))

        my_new_model = User(**my_model_json)

        self.assertTrue(hasattr(my_new_model, "email"))
        self.assertTrue(hasattr(my_new_model, "password"))
        self.assertTrue(hasattr(my_new_model, "first_name"))
        self.assertTrue(hasattr(my_new_model, "last_name"))

        self.assertTrue(hasattr(my_new_model, "id"))
        self.assertTrue(hasattr(my_new_model, "created_at"))
        self.assertTrue(hasattr(my_new_model, "updated_at"))
        self.assertFalse(my_new_model is my_model)


if __name__ == '__main__':
    unittest.main()
