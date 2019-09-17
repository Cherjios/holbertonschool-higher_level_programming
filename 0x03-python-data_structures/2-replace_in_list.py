#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    num = len(my_list)
    if idx < 0:
        return None
    if idx > num:
        return None
    my_list[idx] = element
    return my_list
