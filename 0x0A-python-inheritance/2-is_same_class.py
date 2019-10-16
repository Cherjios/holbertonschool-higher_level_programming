#!/usr/bin/python3
"""Module for is_same_class method"""


def is_same_class(obj, a_class):
    """Function that returns true if the obj is exactly an instance"""
    return type(obj) == a_class
