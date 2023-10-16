#!/usr/bin/python3
"""Defines TestCity class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Defines unittests for models/city.py."""
    def test_instance_creation(self):
        """Test creating an instance of the City class"""
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        """Test setting and accessing class attributes"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        city = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_to_dict(self):
        """Test the to_dict method"""
        city = City()
        city.state_id = "CA"
        city.name = "Los Angeles"
        city_dict = city.to_dict()
        self.assertEqual(city_dict['state_id'], "CA")
        self.assertEqual(city_dict['name'], "Los Angeles")
        self.assertEqual(city_dict['__class__'], 'City')


if __name__ == '__main__':
    unittest.main()
