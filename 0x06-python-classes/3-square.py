#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """A class Square that defines a square."""
    def __init__(self, size=0):
        """initailazing size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Return the current square area"""
        return (self.__size) ** 2
