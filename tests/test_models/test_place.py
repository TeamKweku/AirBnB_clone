#!/usr/bin/python3
'''
Unit test module for the place module.
'''

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    def test_instance(self):
        place1 = Place()
        place2 = Place()
        self.assertIsInstance(place1, Place)
        self.assertIsInstance(place2, Place)

    def test_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_city_id_attribute(self):
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_user_id_attribute(self):
        place = Place()
        self.assertEqual(place.user_id, "")

    # Additional tests for other attributes

    def test_id_type(self):
        place = Place()
        self.assertIsInstance(place.id, str)

    def test_created_at_type(self):
        place = Place()
        self.assertIsInstance(place.created_at, datetime)

    def test_updated_at_type(self):
        place = Place()
        self.assertIsInstance(place.updated_at, datetime)

    def test_to_dict(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
