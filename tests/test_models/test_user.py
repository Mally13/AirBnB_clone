#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Defines unittests for models/user.py."""
    def test_instance_creation(self):
        """Test creating an instance of the User class"""
        user = User()
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """Test setting and accessing class attributes"""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_to_dict(self):
        """Test the to_dict method"""
        user = User()
        user.email = "user@example.com"
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "user@example.com")
        self.assertEqual(user_dict['__class__'], 'User')


if __name__ == '__main__':
    unittest.main()
