#!/usr/bin/python3
"""Module to returns and obj python data structure
    represented by JSON"""
import json


def from_json_string(my_str):
    """Metod to returns an obj python data structue from json string"""
    return json.loads(my_str)
