#!/usr/bin/python3
"""
    ``101-add_attribute`` module
"""


def add_attribute(obj, name, value):
    """
        function ``add_attribute`` to add attirbute to an object
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
