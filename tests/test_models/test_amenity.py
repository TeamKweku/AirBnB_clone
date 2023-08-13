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


if __name__ == "__main__":
    unittest.main()
