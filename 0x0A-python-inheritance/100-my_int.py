#!/usr/bin/python3
"""
    ``100-my_int`` module
"""


class MyInt(int):
    """
        MyInt subclass
    """

    def __eq__(self, other):
        """reverse equal"""
        return int(self) != int(other)

    def __ne__(self, other):
        """reverse equal"""
        return int(self) == int(other)
