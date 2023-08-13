#!/usr/bin/python3
'''
Module to test for the console module
'''

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.console = None
        self.mock_stdout.close()

    def test_count_command(self):
        with patch("models.storage") as mock_storage, \
             patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            mock_storage.get_instance.return_value.count.return_value = 0
            self.console.onecmd("BaseModel.count()")
            self.assertEqual(mock_stdout.getvalue().strip(), "1")


if __name__ == "__main__":
    unittest.main()
