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

    def test_id_type(self):
        state = State()
        self.assertIsInstance(state.id, str)

    def test_created_at_type(self):
        state = State()
        self.assertIsInstance(state.created_at, datetime)

    def test_updated_at_type(self):
        state = State()
        self.assertIsInstance(state.updated_at, datetime)

    def test_to_dict(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
