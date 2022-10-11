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

    def my_print(self):
        """ prints the square with the character #"""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(0, self.__size):
                print('#' * self.__size)
