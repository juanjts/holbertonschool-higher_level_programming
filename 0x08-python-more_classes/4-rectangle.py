#!/usr/bin/python3
"""Rectangle."""


class Rectangle:
    """ Defines a Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        s = ""
        if self.__height == 0 or self.__width == 0:
            return s
        for i in range(self.__height - 1):
            s += '#' * self.__width + '\n'
        s += '#' * self.__width
        return s

    def __repr__(self):
        return "Rectangle(%r, %r)" % (self.__width, self.__height)
