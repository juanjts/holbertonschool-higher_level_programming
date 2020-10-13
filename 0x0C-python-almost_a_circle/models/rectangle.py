#!/usr/bin/python3
""" module task """
from models.base import Base
import json


class Rectangle(Base):
    """ Rectangle class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize method """

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """

        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ height getter """

        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ x getter """

        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ y getter """

        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """

        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ rectangle area """

        return self.__width * self.__height

    def display(self):
        """display the area of Rectangle with #"""

        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ overriding """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id,
                    self.x,
                    self.y,
                    self.width,
                    self.height
                )

    def update(self, *args, **kwargs):
        """ Update the class Rectangle """

        attr = ["id", "width", "height", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        if kwargs is not None or args is None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ function to return the dict representation of a Rectangle """

        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
            }
