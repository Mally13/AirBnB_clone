#!/usr/bin/python3
"""Defines the class TestHBNBCommand"""
import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """class to test the HBNB Command"""
    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()
        self.console.storage = storage

    def tearDown(self):
        """Clean up test environment after each test method is executed"""
        self.console.storage.reload()
        self.console = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """Tests create command"""
        self.console.onecmd("create BaseModel")
        output = mock_stdout.getvalue()
        self.assertIn('\n', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Tests show command"""
        self.console.onecmd("create BaseModel")
        output = mock_stdout.getvalue()
        instance_id = output.strip()
        self.console.onecmd(f"show BaseModel {instance_id}")
        show_output = mock_stdout.getvalue()
        self.assertIn("[BaseModel]", show_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """Tests all command"""
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create City")
        self.console.onecmd("create Place")
        self.console.onecmd("all")
        output = mock_stdout.getvalue()
        self.assertIn("[BaseModel]", output)
        self.assertIn("[City]", output)
        self.assertIn("[Place]", output)

    def test_emptyline(self):
        """Tests empty line behavior"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()
