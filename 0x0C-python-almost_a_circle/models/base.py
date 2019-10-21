#!/usr/bin/python3
"""This module is to define Base Class"""
import json
import os.path


class Base:
    """Defining class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON strng representation"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all attributes alredy set"""
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instance"""
        """1.- Create the file name, 2.- if path file no exits return []
           3.- open the file name, 4.- loop through the file
           5.- return list of ints"""
        filename="{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        list_int= []
        with open(filename, "r") as f:
            dicts = cls.from_json_string(f.readline())
        for i in dicts:
            list_int.append(cls.create(**i))
        return list_int

