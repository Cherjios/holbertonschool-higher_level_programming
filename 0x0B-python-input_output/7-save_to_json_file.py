#!/usr/bin/python3
"""Module that writes an object to a text file
   using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Method to write with json rep"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
