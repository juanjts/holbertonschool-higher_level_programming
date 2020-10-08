#!/usr/bin/python3
"""module space"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""

    with open(filename, mode="a", encoding="UTF8") as f:
        return f.write(text)
