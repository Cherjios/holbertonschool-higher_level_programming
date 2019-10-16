#!/usr/bin/python3
"""Module that creates an object form a JSON file"""

import json


def load_from_json_file(filename):
    """Method to creates an object from a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
