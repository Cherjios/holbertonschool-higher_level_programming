#!/usr/bin/python3
"""Module that returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns the dictionary description for JSON"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
