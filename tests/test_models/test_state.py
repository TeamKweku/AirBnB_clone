#!usr/bin/python3
'''
Module for the unit test of state model
'''

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    def test_instance(self):
        state1 = State()
        state2 = State()
        self.assertIsInstance(state1, State)
        self.assertIsInstance(state2, State)

    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_name_attribute(self):
        state = State()
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()
