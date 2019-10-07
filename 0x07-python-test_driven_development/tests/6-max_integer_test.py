#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer([...])"""

    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_max_num(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([4, 6, 9, 70]), 70)
        self.assertEqual(max_integer([-4, -5, -6, -7, -9]), -4)

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_list_with_only_ints(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_with_not_an_int(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
