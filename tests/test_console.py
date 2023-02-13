#!/usr/bin/env python3
"""
A unit test module for testing ``console.py`` module.
"""

from console import HBNBCommand
import unittest
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """
    Test the basic features of the Console.
    """

    def test_console_helper(self):
        """
        Testing the console helper method, being one of the
        default available command that come with cmd.Cmd.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
        self.assertIn("Documented commands", output)

    def test_create_and_show_on_all_instances(self):
        """
        Testing create and show command against creating
        an instance of BaseModel, User, State, City,
        Amenity, Place, and Review.
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                obj_id = f.getvalue()
                HBNBCommand().onecmd("show {} {}".format(test_class,
                                                         obj_id))
                output = f.getvalue()
                self.assertIn(obj_id, output)

    def test_all_command_output(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        all_class = ['BaseModel', 'User', 'State', 'City',
                     'Amenity', 'Place', 'Review']
        for test_class in all_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(test_class))
                HBNBCommand().onecmd("all")
                output = f.getvalue()
                self.assertIn(test_class, output)

    def test_destroy_command(self):
        """
        This method of this test class tests for exactly
        what the name of the method reads.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            HBNBCommand().onecmd("destroy BaseModel {}".format(obj_id))
            HBNBCommand().onecmd("show BaseModel {}".format(obj_id))
            output = f.getvalue()
        self.assertIn("** no instance found **", output)

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue()
            cmd = "update User {} name hbnb".format(obj_id)
            HBNBCommand().onecmd(cmd)
            HBNBCommand().onecmd("show User {}".format(obj_id))
            output = f.getvalue()
        self.assertIn("'name': 'hbnb'", output)
