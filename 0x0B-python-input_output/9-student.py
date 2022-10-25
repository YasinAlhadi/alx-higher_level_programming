#!/usr/bin/python3
"""
    ``9-student`` module
"""


class Student:
    """class  that defines a student"""

    def __init__(self, first_name, last_name, age):
        """initailize instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            that retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__.copy()
