#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list) - 1
    idx = -1
    while idx >= (-l - 1):
        print("{}".format(my_list[idx]))
        idx -= 1
