#!/usr/bin/python3
"""
    ``0-rectangle`` module contain:
    Rectangle class
    """


class Rectangle:
    """
    Empty class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ initailize width and hieght"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """validate and set rectangle width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """validate and set rectangle height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
