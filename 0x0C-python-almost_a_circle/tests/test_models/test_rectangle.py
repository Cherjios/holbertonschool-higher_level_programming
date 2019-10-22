#!/usr/bin/python3

"""Unittest for models/rectangle.py"""

from models.base import Base
from models.rectangle import Rectangle
import unittest
import sys
import os


class TestRectangle(unittest.TestCase):
    """Test for Class Rectangle"""

    def setUp(self):
        Base._Base__no_objects = 0

    def test00_id(self):
        """Test for empty id"""
        r1 = Rectangle(10, 2, 0, 0, 1)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    """
    def test01_vali_setter(self):
        Test to validate setter
        r1 = Rectangle(10, "2")
        r2 = Rectangle(10, -2)
        r3 = Rectangle(-10, 5)
        self.assertEqual(r1.height(),"[TypeError] height must be an integer")
        """

    def test02_area(self):
        """Test to return the area"""
        r1 = Rectangle(5, 5)
        r2 = Rectangle(20, 10)
        r3 = Rectangle(9, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 25)
        self.assertEqual(r2.area(), 200)
        self.assertEqual(r3.area(), 63)

if __name__ == '__main__':
    unittest.main()
