#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Defines unittests for models/review.py."""
    def test_instance_creation(self):
        """Test creating an instance of the Review class"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """Test setting and accessing class attributes"""
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "A great place to stay."

        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")
        self.assertEqual(review.text, "A great place to stay.")

    def test_inheritance(self):
        """Test if Review inherits from BaseModel"""
        review = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_to_dict(self):
        """Test the to_dict method"""
        review = Review()
        review.text = "Excellent experience."
        review_dict = review.to_dict()
        self.assertEqual(review_dict['text'], "Excellent experience.")
        self.assertEqual(review_dict['__class__'], 'Review')


if __name__ == '__main__':
    unittest.main()
