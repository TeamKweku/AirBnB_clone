#!/usr/bin/python3
'''
Module for the testing the User.
'''

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    '''
    Test for the User class.
    '''

    def test_instance(self):
        user1 = User()
        user2 = User()
        self.assertIsInstance(user1, User)
        self.assertIsInstance(user2, User)

    def test_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_email_attribute(self):
        user = User()
        self.assertEqual(user.email, "")

    def test_password_attribute(self):
        user = User()
        self.assertEqual(user.password, "")

    def test_first_name_attribute(self):
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name_attribute(self):
        user = User()
        self.assertEqual(user.last_name, "")

    def test_id_type(self):
        user = User()
        self.assertIsInstance(user.id, str)

    def test_created_at_type(self):
        user = User()
        self.assertIsInstance(user.created_at, datetime)

    def test_updated_at_type(self):
        user = User()
        self.assertIsInstance(user.updated_at, datetime)

    def test_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
