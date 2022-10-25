#!/usr/bin/python3
"""
    ``1-write_file`` module
"""


def append_write(filename="", text=""):
    """
        function ``append_write`` that append a string a text file
        and return the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
