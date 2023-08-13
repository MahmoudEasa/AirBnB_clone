#!/usr/bin/python3
"""File unittests for console.py"""
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestConsole(unittest.TestCase):
    """Class Test Console
    """

    def test_emptyline(self):
        """Test emptyline
        """
        HBNBCommand.emptyline()
