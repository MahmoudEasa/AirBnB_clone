#!/usr/bin/python3

"""Model to Write a class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place

        Attributes:
            city_id (str): The City.id
            user_id (str): The User.id
            name (str): The Name
            description (str): The Description
            number_rooms (int): The Number Rooms
            number_bathrooms (int): The Number Bathrooms
            max_guest (int): The Max Guest
            price_by_night (int): The Price by Night
            latitude (float): The Latitude
            longitude (float): The Longitude
            amenity_ids (list): The List of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
