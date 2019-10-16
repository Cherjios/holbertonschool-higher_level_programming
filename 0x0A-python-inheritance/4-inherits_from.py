#!/usr/bin/python3
"""Module of sub lcass of"""


def inherits_from(obj, a_class):
    """Function that returns true if the obj is an isntance
       of a class that inherited"""
    if type(obj) != a_class:
        return isinstance(obj, a_class)
