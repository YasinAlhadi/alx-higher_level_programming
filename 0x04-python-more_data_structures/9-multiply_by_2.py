#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    for i, j in sorted(a_dictionary.items()):
        new_dict[i] = j * 2
        """
        print('{} : {:d}'.format(i, j * 2))
        """
    return new_dict