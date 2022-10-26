#!/usr/bin/python3
"""
    ``10-student`` module
"""


class Student:
    """class  that defines a student"""

    def __init__(self, first_name, last_name, age):
        """initailize instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            that retrieves a dictionary representation of a Student instance.
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {i: j for i, j in self.__dict__.items() if i in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """
            replace all attributes of the Student instance.
        """
        for i, j in json.items():
            self.__dict__[i] = j
