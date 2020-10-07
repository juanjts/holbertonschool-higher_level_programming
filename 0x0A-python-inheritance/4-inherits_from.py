#!/usr/bin/python3
"""module space"""


def inherits_from(obj, a_class):
    """inherits_from a_class or not"""

    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False
