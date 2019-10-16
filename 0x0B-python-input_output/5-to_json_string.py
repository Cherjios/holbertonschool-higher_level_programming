#!/usr/bin/python3
"""Module to returns the JSON representation fo an obj
   string"""
import json


def to_json_string(my_obj):
    """Metod to return the json representation of a
       obj (string)"""
    return json.dumps(my_obj)
