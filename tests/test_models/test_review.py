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

if __name__ == "__main__":
    unittest.main()
