#!usr/bin/python3
'''
Module to test the file storage module.
'''

import unittest
import os
from models import storage
from console import HBNBCommand
from io import StringIO
import sys


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        self.assertEqual(storage._FileStorage__file_path, "tests.json")

    def test_objects_dict_exists(self):
        self.assertTrue(hasattr(storage, '_FileStorage__objects'))
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all_method(self):
        objs = storage.all()
        self.assertIsInstance(objs, dict)
        self.assertIs(objs, storage._FileStorage__objects)

    def test_new_method(self):
        from models.base_model import BaseModel
        new_base = BaseModel()
        storage.new(new_base)
        key = "{}.{}".format(new_base.__class__.__name__, new_base.id)
        self.assertTrue(key in storage.all())

    def test_reload_method(self):
        storage.reload()
        objs = storage.all()
        self.assertIsInstance(objs, dict)


if __name__ == "__main__":
    unittest.main()
