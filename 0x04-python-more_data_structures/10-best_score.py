#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        biggest_s = max(list(a_dictionary.keys()))
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[biggest_s]:
                biggest_s = key
        return biggest_s
    return None
