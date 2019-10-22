#!/usr/bin/python3

"""Unittest for models/square.py"""

from models.base import Base
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """Test for Class Square"""

    def setUp(self):
        Base._Base__no_objects = 0

if __name__ == '__main__':
    unittest.main()
