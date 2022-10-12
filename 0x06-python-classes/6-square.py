#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """A class Square that defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """initailazing size"""
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        for x in range(self.__position[1]):
            print()
        for y in range(0, self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))
