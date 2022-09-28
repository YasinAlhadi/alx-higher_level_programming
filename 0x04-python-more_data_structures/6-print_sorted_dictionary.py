#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_keys = sorted(a_dictionary)
    for i in s_keys:
        print('{:s} : {}'.format(i, a_dictionary[i]))
