#!/usr/bin/python3

"""Unittest for models/rectangle.py"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import sys
import os


class TestRectangle(unittest.TestCase):
    """Test for Class Rectangle"""

    def setUp(self):
        Base._Base__no_objects = 0

    def test00_id(self):
        """Test for empty id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 3)
  
    def test01_id(self):
        """Test for given int id"""
        r1 = Rectangle(10, 2, 0, 0, 5)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 12)

    def test02_id(self):
        """Test for given sti id"""
        r1 = Rectangle(10, 2, 0, 0, "A5")
        r2 = Rectangle(10, 2, 0, 0, "B12")
        self.assertEqual(r1.id, "A5")
        self.assertEqual(r2.id, "B12")

    def test01_vali_setter_with(self):
        """Test to validate setter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)

    def test02_vali_setter_with(self):
        with self.assertRaises(ValueError):
            r2 = Rectangle(-10, 2)

    def test01_vali_setter_height(self):
        """Test to validate setter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")

    def test02_vali_setter_height(self):
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, -2)

    def test01_vali_setter_x(self):
        """Test to validate setter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, "3", 4)

    def test02_vali_setter_x(self):
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 2, -2, 5)

    def test01_vali_setter_y(self):
        """Test to validate setter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, "4")

    def test02_vali_setter_y(self):
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 2, 2, -5)
          
    def test_Rectangle_area(self):
        """Test to return the area"""
        r1 = Rectangle(5, 5)
        r2 = Rectangle(20, 10)
        r3 = Rectangle(9, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 25)
        self.assertEqual(r2.area(), 200)
        self.assertEqual(r3.area(), 63)


    def test_inheritance_from_Base(self):
        """ Check inheritance from square """
        self.assertTrue(issubclass(Rectangle, Base))
    
if __name__ == '__main__':
    unittest.main()
