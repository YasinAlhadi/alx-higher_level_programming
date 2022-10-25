#!/usr/bin/python3
"""
    ``8-my_class`` module
"""


def class_to_json(obj):
    """define class_to_json"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return ()
