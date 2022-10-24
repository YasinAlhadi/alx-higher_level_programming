#!/usr/bin/python3
"""
    ``5-base_geometry`` module
"""


class BaseGeometry:
    """
        define BaseGeometry: empty class
    """
    def area(self):
        """
            method ``area`` raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            method ``integer_validator``  that validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
