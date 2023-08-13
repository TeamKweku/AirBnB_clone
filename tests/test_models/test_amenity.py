#!/usr/bin/python3
'''
Test Module fro the Amenity module
'''

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    def test_instance(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertIsInstance(amenity1, Amenity)
        self.assertIsInstance(amenity2, Amenity)

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_name_attribute(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_id_type(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

    def test_created_at_type(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at_type(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("name", amenity_dict)
        self.assertIn("__class__", amenity_dict)
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
