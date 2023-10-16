#!/usr/bin/python3
"""Defines TestAmenity class to test Amenities"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Defines unittests for models/amenity.py."""
    def test_default_name(self):
        """
        Test that the 'name' attribute of an Amenity instance has
        the default value (an empty string).
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_set_name(self):
        """
        Test that you can set the 'name' attribute of an Amenity
        instance and retrieve it correctly.
        """
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_inheritance(self):
        """
        Test that Amenity inherits from BaseModel and has the expected methods.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "to_dict"))
        self.assertTrue(hasattr(amenity, "__str__"))


if __name__ == '__main__':
    unittest.main()
