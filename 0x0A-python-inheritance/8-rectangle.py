#!/usr/bin/python3
"""module space"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class from BaseGeometry"""

    def __init__(self, width, height):
        """initialize method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
