#!/usr/bin/python3
""" module space"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, value):
        """initialize method"""

        int.__init__(self)
        if type(value) is int:
            self.__value = value

    def __eq__(self, other):
        return self.__value != other

    def __ne__(self, other):
        return self.__value == other
