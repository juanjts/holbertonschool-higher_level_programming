#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic2 = a_dictionary.copy()
    for i in dic2:
        dic2[i] *= 2
    return dic2
