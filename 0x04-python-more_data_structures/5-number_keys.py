#!/usr/bin/python3
def number_keys(a_dictionary):
    nb_keys = 0
    for i, j in enumerate(a_dictionary):
        nb_keys += i
    return nb_keys
