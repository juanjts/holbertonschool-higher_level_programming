#!/usr/bin/python3
"""module space"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square class"""

    def __init__(self, size):
        """initialize method"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
