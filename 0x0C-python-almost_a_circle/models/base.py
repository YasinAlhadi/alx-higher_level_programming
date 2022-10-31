#!/usr/bin/python3
"""base mudole"""
import json
import os


class Base:
    """define Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initailixze id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method ``to_dicctionart``that returns the JSON string
        representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ ``class method save to file`` that writes the JSON string
        representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ static metho From_json_string`` that returns the list
        of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ class method ``create`` that returns an instance
        with all attributes already set """
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        elif cls.__name__ == 'Square':
            new = cls(1)
        cls.update(new, **dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ class mehotd `` load_from_file`` that returns a list
        of instances """
        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
