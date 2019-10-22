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
        
    def tearDown(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

if __name__ == '__main__':
    unittest.main()
