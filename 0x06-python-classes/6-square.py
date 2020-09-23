#!/usr/bin/python3
"""documentation"""


class Square:
    """documentation"""

    def __init__(self, size=0, position=(0, 0)):
        """documentation"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """documentation"""

        return(self.__position)

    @position.setter
    def position(self, value):
        """documentation"""

        if len(value) != 2 and type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int and type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """documentation"""

        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for pos in range(self.__position[0])]), end="")
            print("".join(["#" for sizz in range(self.__size)]))
