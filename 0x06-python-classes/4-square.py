#!/usr/bin/python3
"""documentation"""


class Square:
    """documentation"""

    def __init__(self, size=0):
        """documentation"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """documentation"""

        return(self.__size * self.__size)

    @property
    def size(self):
        """documentation"""

        return self.__size

    @size.setter
    def size(self, set_size):
        """documentation"""

        if isinstance(set_size, int):
            if set_size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = set_size
        else:
            raise TypeError("size must be an integer")
