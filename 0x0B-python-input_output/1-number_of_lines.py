#!/usr/bin/python3
"""module space"""


def number_of_lines(filename=""):
    """number of lines"""

    with open(filename, encoding='utf-8') as f:
        return sum(1 for line in f)
