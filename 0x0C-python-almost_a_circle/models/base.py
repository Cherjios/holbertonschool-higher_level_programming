#!/usr/bin/python3
"""This module is to define Base Class"""
import json
import os.path
import csv


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
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        list_int = []
        with open(filename, "r") as f:
            dicts = cls.from_json_string(f.readline())
        for i in dicts:
            list_int.append(cls.create(**i))
        return list_int

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV."""
        if type(list_objs) != list and list_objs is not None \
                or not all(isinstance(x, cls) for x in list_objs):
            raise TypeError("list_objs must be a list")
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w") as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                rec_fields = ['id', 'width', 'height', 'x', 'y']
                squ_fields = ['id', 'size', 'x', 'y']
                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(f, fieldnames=rec_fields)
                else:
                    writer = csv.DictWriter(f, fieldnames=squ_fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV."""
        filename = "{}.csv".format(cls.__name__)
        rec_header = ["id", "width", "height", "x", "y"]
        squ_header = ["id", "size", "x", "y"]
        header = rec_header if cls.__name__ == "Rectangle" else squ_header
        res = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter=',')
                for i, row in enumerate(reader):
                    if i > 0:
                        new = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(new, header[j], int(e))
                        res.append(new)
        return res
