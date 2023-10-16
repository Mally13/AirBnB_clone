#!/usr/bin/python3
"""Defines unittests for models/statepy."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Defines unittests for models/state.py."""
    def test_instance_creation(self):
        """Test creating an instance of the State class"""
        state = State()
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """Test setting and accessing class attributes"""
        state = State()
        state.name = "Machakos"

        self.assertEqual(state.name, "Machakos")

    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        state = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_to_dict(self):
        """Test the to_dict method"""
        state = State()
        state.name = "Nairobi"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], "Nairobi")
        self.assertEqual(state_dict['__class__'], 'State')


if __name__ == '__main__':
    unittest.main()
