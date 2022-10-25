#!/usr/bin/python3
"""
    ``1-write_file`` module
"""


def write_file(filename="", text=""):
    """
        function ``write_file`` that write a string a text file
        and return the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
