#!/usr/bin/python3
"""
    ``8-rectangle`` module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        subclass ``Rectangle`` that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """initailize width and hieght"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
            method area returns area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
            return rectangle description
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
