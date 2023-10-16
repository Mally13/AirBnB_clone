#!/usr/bin/python3
"""Defines Unittests for testing methods of the FileStorage class."""
import unittest
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.state import State
from models import storage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""
    def test_all(self):
        """Test the all method of FileStorage"""
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test the new method of FileStorage"""
        model = BaseModel()
        storage.new(model)
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIsNotNone(storage.all().get(key))

    def test_save_and_reload(self):
        """Test the save and reload methods of FileStorage"""
        model = BaseModel()
        key = f"{model.__class__.__name__}.{model.id}"
        storage.new(model)
        storage.save()

        os.remove(storage._FileStorage__file_path)

        storage.reload()
        self.assertIsNotNone(storage.all().get(key))


if __name__ == '__main__':
    unittest.main()
