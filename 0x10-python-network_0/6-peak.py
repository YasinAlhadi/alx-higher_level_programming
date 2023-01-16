#!/usr/bin/python3
"""6-peek module"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if len(list_of_integers) < 3:
        return None
    peek = list_of_integers[1]
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] >= peek:
            peek = list_of_integers[i]
    return peek
