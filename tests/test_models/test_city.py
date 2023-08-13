#!/usr/bin/python3
'''
Module to test the city module in base model library
'''

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    def test_instance(self):
        city1 = City()
        city2 = City()
        self.assertIsInstance(city1, City)
        self.assertIsInstance(city2, City)

    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_state_id_attribute(self):
        city = City()
        self.assertEqual(city.state_id, "")

    def test_name_attribute(self):
        city = City()
        self.assertEqual(city.name, "")

    def test_id_type(self):
        city = City()
        self.assertIsInstance(city.id, str)

    def test_created_at_type(self):
        city = City()
        self.assertIsInstance(city.created_at, datetime)

    def test_updated_at_type(self):
        city = City()
        self.assertIsInstance(city.updated_at, datetime)

    def test_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("__class__", city_dict)
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
