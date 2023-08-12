"""Test cases for base model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):
    """Outlines various test cases for the class attributes and mehtods"""

    def test_instance(self):
        """testing for type of class"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertEqual(type(base1), BaseModel)
        self.assertEqual(type(base2), BaseModel)

    def test_type_id(self):
        """test to check type of id attribute"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base2.id), str)

    def test_unique_id(self):
        """test for unique id in the instances"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_created_at(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base2.created_at, datetime)

    def test_updated_at(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base1.updated_at, datetime)
        self.assertIsInstance(base2.updated_at, datetime)

    def test_none_passed(self):
        """checking when none is passed"""
        base1 = BaseModel(None)
        self.assertNotIn(None, base1.__dict__.keys())

    def test_empty_dict(self):
        dicts = {}
        base1 = BaseModel(**dicts)
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)
        self.assertNotIn("__class__", base1.__dict__.keys())

    def test_str(self):
        user1 = BaseModel()
        string_rep = str(user1)
        self.assertIsInstance(string_rep, str)


class TestBaseModelSave(unittest.TestCase):
    """a class to test the save method"""

    def setUp(self):
        """setup file and dict object every run of test"""
        with open("tests.json", "w"):
            FileStorage._FileStorage__file_path = "tests.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """destroy after running test"""
        try:
            os.remove("tests.json")
        except FileNotFoundError:
            pass

    def test_save(self):
        """test save method"""
        base1 = BaseModel()
        base1.save()
        self.assertNotEqual(base1.created_at, base1.updated_at)

    def test_save_None(self):
        """testing case of None"""
        base1 = BaseModel()
        with self.assertRaises(TypeError):
            base1.save(None)

    def test_save_stored_in_file(self):
        """test if instance is stored in file on save"""
        base2 = BaseModel()
        base2.save()
        id = f"BaseModel.{base2.id}"

        with open("tests.json", "r") as file:
            self.assertIn(id, file.read())


class TestToDict(unittest.TestCase):
    """tests for the to_dict method of the BaseModel class"""

    def test_to_dict(self):
        """test to_dict method"""
        base1 = BaseModel()
        new_dict = base1.to_dict()
        self.assertIsInstance(new_dict, dict)
        self.assertIn("created_at", new_dict)
        self.assertIn("updated_at", new_dict)
        self.assertIn("__class__", new_dict)
        self.assertIn("id", new_dict)
        self.assertNotIn("django", new_dict)
        self.assertNotIn("victor", new_dict)

    def test_to_dict_class_types(self):
        """check for type of attributes"""
        base1 = BaseModel()
        dicts = base1.to_dict()
        self.assertIsInstance(dicts["created_at"], str)
        self.assertIsInstance(dicts["updated_at"], str)
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)
        self.assertEqual(dicts["created_at"], base1.created_at.isoformat())
        self.assertEqual(dicts["updated_at"], base1.updated_at.isoformat())

    def test_to_dict_added_attributes(self):
        """check if attributes are added to dict"""
        base1 = BaseModel()
        base1.name = "django"
        base1.email = "djangotuts@alx.com"
        self.assertIn("name", base1.to_dict())
        self.assertIn("email", base1.to_dict())

    def test_to_dict_invalid_type(self):
        """test case of wrong time to_dict"""
        base1 = BaseModel()
        with self.assertRaises(TypeError):
            base1.to_dict(None)
