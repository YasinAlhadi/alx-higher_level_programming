#!/usr/bin/python3
"""square mudole"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initailize instances"""
        super().__init__(size, size, x, y, id=None)

    def __str__(self):
        """method that returns [Square]
        (<id>) <x>/<y> - <width>/<height>"""
        return "[{}] ({}) {}/{} - {}"\
            .format(type(self).__name__, self.id, self.x, self.y,
                    self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """method ``update`` that assigns an argument to each attribute"""
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        elif len(kwargs) > 0:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                if i == 'size':
                    self.size = j
                if i == 'x':
                    self.x = j
                if i == 'y':
                    self.y = j

    def to_dictionary(self):
        """metho ``to_dictionary`` that returns the dictionary
        representation of a Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
