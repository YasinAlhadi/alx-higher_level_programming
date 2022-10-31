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
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """method area that returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """that prints in stdout the Rectangle
        instance with the character '#'."""
        rect = "\n" * self.__y + (" " * self.x + "#" * self.width + '\n') *\
        self.__height
        print(rect, end="")

    def __str__(self):
        """method that returns [Rectangle]
        (<id>) <x>/<y> - <width>/<height>"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """method update that assigns an argument to each attribute"""
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                   self.id = arg
                if i == 1:
                   self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif len(kwargs) > 0:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                if i == 'width':
                    self.width = j
                if i == 'height':
                    self.height = j
                if i == 'x':
                    self.x = j
                if i == 'y':
                    self.y = j

    def to_dictionary(self):
        """ ``to_dictionary`` that returns the dictionary
        representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width,
                 'height': self.__height, 'x': self.__x, 'y': self.__y}
