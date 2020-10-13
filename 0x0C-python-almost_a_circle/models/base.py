#!/usr/bin/python3
""" module task """
import json


class Base:
    """ class with private nb_obj """

    __nb_objects = 0

    def __init__(self, id=None):
        """inicialize method """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string """

        if not list_dictionaries or list_dictionaries == []:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file """

        new = []
        if list_objs is not None:
            for i in list_objs:
                new.append(cls.to_dictionary(i))

        filename = str(cls.__name__ + ".json")

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """

        if not json_string or json_string == "":
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to Instance """

        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ File to instances """

        name = str(cls.__name__) + '.json'
        try:
            with open(name, 'r+', encoding='utf-8') as f:
                y = cls.from_json_string(f.read())
            ls = []
            for instance in y:
                ls.append(cls.create(**instance))
            return ls
        except Exception:
            return []
