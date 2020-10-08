#!/usr/bin/python3
"""module space"""


def write_file(filename="", text=""):
    """function to write a string"""

    with open(filename, mode="w", encoding="UTF8") as f:
        return f.write(text)
