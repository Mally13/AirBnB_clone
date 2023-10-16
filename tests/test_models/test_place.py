#!/usr/bin/python3
"""Defines TestPlace class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Defines unittests for models/place.py."""
    def test_instance_creation(self):
        """Test creating an instance of the Place class"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test setting and accessing class attributes"""
        place = Place()
        place.city_id = "12345"
        place.user_id = "67890"
        place.name = "Cozy Cabin"
        place.description = "A lovely cabin in the woods."
        place.number_rooms = 2
        place.number_bathrooms = 1.5
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["wifi", "pool", "kitchen"]

        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "67890")
        self.assertEqual(place.name, "Cozy Cabin")
        self.assertEqual(place.description, "A lovely cabin in the woods.")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1.5)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["wifi", "pool", "kitchen"])

    def test_inheritance(self):
        """Test if Place inherits from BaseModel"""
        place = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_to_dict(self):
        """Test the to_dict method"""
        place = Place()
        place.name = "Cottage"
        place_dict = place.to_dict()
        self.assertEqual(place_dict['name'], "Cottage")
        self.assertEqual(place_dict['__class__'], 'Place')


if __name__ == '__main__':
    unittest.main()
