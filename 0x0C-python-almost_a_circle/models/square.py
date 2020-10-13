#!/usr/bin/python3
""" module task """
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """ Class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize method """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str method return from square class """

        return "[Square] ({}) {}/{} - {}".format(
                    self.id,
                    self.x,
                    self.y,
                    self.size
                )

    @property
    def size(self):
        """ size getter """

        return self.width

    @size.setter
    def size(self, value):
        """ size setter """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the class Square """

        attr = ["id", "size", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        if kwargs is not None or args is None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ instance to dictionary representation """

        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.size
            }
