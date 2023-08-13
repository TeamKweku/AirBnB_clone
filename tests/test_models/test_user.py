#!/usr/bin/python3
'''
Module for the testing the User.
'''
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
