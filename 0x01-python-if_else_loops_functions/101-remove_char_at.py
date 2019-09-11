#!/usr/bin/python3
def remove_char_at(str, n):
    strcp = ""
    for i, v in enumerate(str):
        if i is n:
            strcp += ""
        else:
            strcp += v
    return strcp
