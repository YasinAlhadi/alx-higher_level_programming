#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """A class Square that defines a square."""
    def __init__(self, size=0):
        """initailazing size"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Return the current square area"""
        return (self.__size) ** 2
