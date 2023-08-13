#!/usr/bin/python3

"""Module to test the FileStorage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Class Test FileStorage
    """

    def setUp(self):
        """Set up for the tests"""
        self.fs = FileStorage()
        self.new_instance = BaseModel()

    def test_all(self):
        """Function to test FileStorage
        """
        self.fs.new(self.new_instance)
        self.fs.save()
        self.fs.reload()
        obj = self.fs.all()
        self.assertEqual(type(obj), dict)

    def test_save(self):
        """Test save"""

        pass

    def test_reload(self):
        """ Test reload"""
        pass


if __name__ == '__main__':
    unittest.main()
