#!/usr/bin/python3
"""module space"""


def read_file(filename=""):
    """function to read file"""

    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
