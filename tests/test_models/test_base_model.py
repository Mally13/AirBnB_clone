#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Defines unittests for models/base_model.py."""
    def test_init(self):
        """Test the __init__ method of BaseModel"""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_save(self):
        """Test the save method of BaseModel"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        model = BaseModel()
        model_str = str(model)
        self.assertIn('BaseModel', model_str)
        self.assertIn(str(model.id), model_str)


if __name__ == '__main__':
    unittest.main()
