#!/usr/bin/python3
"""rectangle mudole"""
from models.base import Base


class Rectangle(Base):
    """define Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initailixze iinstances"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @width.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @width.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def validator(sel, name, value, xy=True):
        """method to validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if not xy and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if xy and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """method area that returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """that prints in stdout the Rectangle
        instance with the character '#'."""
        rect = (("#" * self.width + '\n') * self.__height)[:-1]
        print(rect)
