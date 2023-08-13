#!/usr/bin/python3

"""Module to test the Place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class Test Place
    """

    def test_place(self):
        """Function to test Place
        """
        my_model = Place()
        my_model.city_id = "city_id"
        my_model.user_id = "user_id"
        my_model.name = "My Place"
        my_model.description = "description"
        my_model.number_rooms = 0
        my_model.number_bathrooms = 0
        my_model.max_guest = 0
        my_model.price_by_night = 0
        my_model.latitude = 0.0
        my_model.longitude = 0.0
        my_model.amenity_ids = []

        self.assertTrue(hasattr(my_model, "city_id"))
        self.assertTrue(hasattr(my_model, "user_id"))
        self.assertTrue(hasattr(my_model, "name"))
        self.assertTrue(hasattr(my_model, "description"))
        self.assertTrue(hasattr(my_model, "number_rooms"))
        self.assertTrue(hasattr(my_model, "number_bathrooms"))
        self.assertTrue(hasattr(my_model, "max_guest"))
        self.assertTrue(hasattr(my_model, "price_by_night"))
        self.assertTrue(hasattr(my_model, "latitude"))
        self.assertTrue(hasattr(my_model, "longitude"))
        self.assertTrue(hasattr(my_model, "amenity_ids"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

        self.assertTrue(type(my_model.city_id) == str)
        self.assertTrue(type(my_model.user_id) == str)
        self.assertTrue(type(my_model.name) == str)
        self.assertTrue(type(my_model.description) == str)
        self.assertTrue(type(my_model.number_rooms) == int)
        self.assertTrue(type(my_model.number_bathrooms) == int)
        self.assertTrue(type(my_model.max_guest) == int)
        self.assertTrue(type(my_model.price_by_night) == int)
        self.assertTrue(type(my_model.latitude) == float)
        self.assertTrue(type(my_model.longitude) == float)
        self.assertTrue(type(my_model.amenity_ids) == list)

        my_model_json = my_model.to_dict()

        self.assertTrue(hasattr(my_model_json, "__class__"))

        my_new_model = Place(**my_model_json)

        self.assertTrue(hasattr(my_new_model, "city_id"))
        self.assertTrue(hasattr(my_new_model, "user_id"))
        self.assertTrue(hasattr(my_new_model, "name"))
        self.assertTrue(hasattr(my_new_model, "description"))
        self.assertTrue(hasattr(my_new_model, "number_rooms"))
        self.assertTrue(hasattr(my_new_model, "number_bathrooms"))
        self.assertTrue(hasattr(my_new_model, "max_guest"))
        self.assertTrue(hasattr(my_new_model, "price_by_night"))
        self.assertTrue(hasattr(my_new_model, "latitude"))
        self.assertTrue(hasattr(my_new_model, "longitude"))
        self.assertTrue(hasattr(my_new_model, "amenity_ids"))

        self.assertTrue(hasattr(my_new_model, "id"))
        self.assertTrue(hasattr(my_new_model, "created_at"))
        self.assertTrue(hasattr(my_new_model, "updated_at"))
        self.assertFalse(my_new_model is my_model)

        self.assertTrue(type(my_new_model.city_id) == str)
        self.assertTrue(type(my_new_model.user_id) == str)
        self.assertTrue(type(my_new_model.name) == str)
        self.assertTrue(type(my_new_model.description) == str)
        self.assertTrue(type(my_new_model.number_rooms) == int)
        self.assertTrue(type(my_new_model.number_bathrooms) == int)
        self.assertTrue(type(my_new_model.max_guest) == int)
        self.assertTrue(type(my_new_model.price_by_night) == int)
        self.assertTrue(type(my_new_model.latitude) == float)
        self.assertTrue(type(my_new_model.longitude) == float)
        self.assertTrue(type(my_new_model.amenity_ids) == list)


if __name__ == '__main__':
    unittest.main()
