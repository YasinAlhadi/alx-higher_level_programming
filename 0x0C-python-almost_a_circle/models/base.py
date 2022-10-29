#!/usr/bin/python3
"""base mudole"""


class Base:
    """define Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initailixze id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
