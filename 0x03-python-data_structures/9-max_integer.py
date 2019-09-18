#!/usr/bin/python3
def max_integer(my_list=[]):
    maxn = 0
    if my_list == "":
        return None
    for i in my_list:
        if my_list[i] > maxn:
            maxn = my_list[i]
        return maxn
