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

    def my_print(self):
        """documentation"""

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

    @property
    def size(self):
        """documentation"""

        return self.__size

    @size.setter
    def size(self, value):
        """documentation"""

        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
