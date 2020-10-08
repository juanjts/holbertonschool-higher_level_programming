#!/usr/bin/python3
"""module space"""


def read_lines(filename="", nb_lines=0):
    """function to print lines of a file"""

    with open(filename, encoding="UTF8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        i = 0
        while i < nb_lines:
            print(f.readline(), end="")
            i += 1
