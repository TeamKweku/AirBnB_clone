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

if __name__ == "__main__":
    unittest.main()
