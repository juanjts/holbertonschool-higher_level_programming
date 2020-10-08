#!/usr/bin/python3
"""module space"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """initialize method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """initialize method"""

        if attrs is not None:
            dic = {}
            for i in attrs:
                if hasattr(self, i):
                    dic[i] = getattr(self, i)
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        """initialize method"""

        for i in json:
            self.__dict__[i] = json[i]
