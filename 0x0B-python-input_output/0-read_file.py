#!/usr/bin/python3
"""
    ``0-read_file`` module
"""


def read_file(filename=""):
    """
        function ``read_file`` that reads a text file
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
