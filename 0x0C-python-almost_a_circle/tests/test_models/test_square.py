#!/usr/bin/python3

"""Unittest for models/square.py"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """Test for Class Square"""

    def setUp(self):
        Base._Base__no_objects = 0

    def test_square_test(self):
        """ Check Type of square object """
        s1 = Square(3)
        s2 = Square(2)
        s3 = Square(5)
        self.assertEqual(type(s1), Square)
        self.assertEqual(type(s2), Square)
        self.assertEqual(type(s3), Square)

    def test00_vali_setter_size(self):
        """Test to validate setter size"""
        with self.assertRaises(TypeError):
            s1 = Square("2")

    def test01_vali_setter_size(self):
        """Test to validate setter size"""
        with self.assertRaises(ValueError):
            s1 = Square(-2)

    def test00_vali_setter_x(self):
        """Test to validate setter x"""
        with self.assertRaises(TypeError):
            s1 = Square(2, "2")

    def test01_vali_setter_x(self):
        """Test to validate setter x"""
        with self.assertRaises(ValueError):
            s1 = Square(2, -2)

    def test00_vali_setter_y(self):
        """Test to validate setter y"""
        with self.assertRaises(TypeError):
            s1 = Square(2, 3, "2")

    def test01_vali_setter_x(self):
        """Test to validate setter y"""
        with self.assertRaises(ValueError):
            s1 = Square(2, 8, -2)

    def test_inheritance_from_Rectangle(self):
        """ Check inheritance from rectangle """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_inheritance_from_Square(self):
        """ Check inheritance from square """
        self.assertTrue(issubclass(Square, Base))

    def test_Square_area(self):
        """ Check Type of square object """
        s1 = Square(3)
        s2 = Square(2)
        s3 = Square(5)
        self.assertEqual(s1.area(), 9)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 25)

if __name__ == '__main__':
    unittest.main()
