#!/usr/bin/python3
"""``0-add_integer`` module:
    contain add_ineger function
    return addition a and b
    a and b must be integers or floats
    a and b must be first casted to integers if they are float"""


def add_integer(a, b=98):
    """``add_ineger()`` function
    Returns an integer
    the addition of a and b"""
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


"""if __name__ == "__main__":
    import doctest
    doctest.tesetfile("tests/0-add_integer.txt")"""
