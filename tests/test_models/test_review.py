#!/usr/bin/python3

"""Module to test the review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class Test Review
    """

    def test_review(self):
        """Function to test review
        """
        my_model = Review()
        my_model.text = "My Review"
        my_model.place_id = 89
        my_model.user_id = 2

        self.assertTrue(hasattr(my_model, "text"))
        self.assertTrue(hasattr(my_model, "place_id"))
        self.assertTrue(hasattr(my_model, "user_id"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

        my_model_json = my_model.to_dict()

        self.assertTrue(hasattr(my_model_json, "__class__"))

        my_new_model = Review(**my_model_json)

        self.assertTrue(hasattr(my_new_model, "text"))
        self.assertTrue(hasattr(my_new_model, "place_id"))
        self.assertTrue(hasattr(my_new_model, "user_id"))
        self.assertTrue(hasattr(my_new_model, "id"))
        self.assertTrue(hasattr(my_new_model, "created_at"))
        self.assertTrue(hasattr(my_new_model, "updated_at"))
        self.assertFalse(my_new_model is my_model)


if __name__ == '__main__':
    unittest.main()
