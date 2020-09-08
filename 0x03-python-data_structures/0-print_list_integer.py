#!/usr/bin/python3
def print_list_integer(my_list=[]):
    l = len(my_list) - 1
    i = 0
    while i <= l:
        print("{:d}".format(my_list[i]))
        i += 1
