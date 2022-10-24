#!/usr/bin/python3
"""
    ``10-square`` module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        subclass that inherits from Rectangle
    """
    def __init__(self, size):
        """initailize size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
            return rectangle description
        """
        return self.__size ** 2

    def __str__(self):
        """
            return squre description
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
