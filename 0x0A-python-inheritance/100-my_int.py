#!/usr/bin/python3
"""Module for MyInt"""


class MyInt(int):
    def __eq__(self, other):
        """equal self == other"""
        return int(self) != int(other)

    def __ne__(self, other):
        """no equal self != other"""
        return int(self) == int(other)
