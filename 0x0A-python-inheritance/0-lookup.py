#!/usr/bin/python3
"""
    ``0-lookup`` module
"""


def lookup(obj):
    """
    lookup function: returns the list of available attribute
    s and methods of an object.
    """
    return dir(obj)
