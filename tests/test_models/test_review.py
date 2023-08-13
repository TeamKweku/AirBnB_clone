#!/usr/bin/python3
'''
Module for unit testing review module.
'''

import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    def test_instance(self):
        review1 = Review()
        review2 = Review()
        self.assertIsInstance(review1, Review)
        self.assertIsInstance(review2, Review)

    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_place_id_attribute(self):
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_id_attribute(self):
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_text_attribute(self):
        review = Review()
        self.assertEqual(review.text, "")

    def test_id_type(self):
        review = Review()
        self.assertIsInstance(review.id, str)

    def test_created_at_type(self):
        review = Review()
        self.assertIsInstance(review.created_at, datetime)

    def test_updated_at_type(self):
        review = Review()
        self.assertIsInstance(review.updated_at, datetime)

    def test_to_dict(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)
        self.assertIn("__class__", review_dict)
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
