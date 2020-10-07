#!/usr/bin/python3
"""module space"""


class BaseGeometry:
    """raise exceptions"""

    def area(self):
        """print exception if no area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """is an integer validator fot type or value error"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
