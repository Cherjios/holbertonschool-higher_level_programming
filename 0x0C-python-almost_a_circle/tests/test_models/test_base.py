#!/usr/bin/python3

"""Unittest for models/base.py"""

from models.base import Base
import unittest
import os


class TestBase(unittest.TestCase):
    """Tests for Class Base"""

    def setUp(self):
        Base._Base__no_objects = 0

    def test00_id(self):
        """Test for id empty."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test01_id(self):
        """Test for correct id attribute."""
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(5)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 5)

    def test02_id(self):
        """Test for str id."""
        b1 = Base("a")
        b2 = Base("xx")
        b3 = Base("Q-b")
        b4 = Base("QWE")
        self.assertEqual(b1.id, "a")
        self.assertEqual(b2.id, "xx")
        self.assertEqual(b3.id, "Q-b")
        self.assertEqual(b4.id, "QWE")

    def test03_id(self):
        """Test for negative id numbers"""
        b1 = Base(-1)
        b2 = Base(-15)
        b3 = Base(-100)
        self.assertEqual(b1.id, -1)
        self.assertEqual(b2.id, -15)
        self.assertEqual(b3.id, -100)

    def test04_id(self):
        """Test for float id numbers"""
        b1 = Base(1.5)
        b2 = Base(0.55)
        b3 = Base(-.25)
        self.assertEqual(b1.id, 1.5)
        self.assertEqual(b2.id, 0.55)
        self.assertEqual(b3.id, -.25)

    def test_one_argument(self):
        """ test a base with 1 argument """
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_two_arguments(self):
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_dict_to_json_none(self):
        """ test dict to json none """
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_dict_to_json_empty(self):
        """ test empty dict to  json """
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_dict_from_json_none(self):
        """ test dict to json none """
        self.assertEqual(Base.from_json_string(None), [])

    def test_dict_from_json_empty(self):
        """ test empty dict to  json """
        self.assertEqual(Base.from_json_string(""), [])

if __name__ == '__main__':
    unittest.main()
