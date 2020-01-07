#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    for i in range(len(list_of_integers)):
        if list_of_integers is None or len(list_of_integers) == 0:
            return None
        if list_of_integers[i+1] > list_of_integers[i] and \
                list_of_integers[i + 1] > list_of_integers[i + 2]:
            return list_of_integers[i + 1]
        elif list_of_integers[i+1] == list_of_integers[i] or \
                list_of_integers[i + 1] == list_of_integers[i + 2]:
            return list_of_integers[i + 1]
        else:
            continue
