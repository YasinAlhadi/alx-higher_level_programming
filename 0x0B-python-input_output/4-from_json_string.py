#!/usr/bin/python3
"""
    ``4-from_json_string`` module
"""
import json


def from_json_string(s_my_list):
    """
        function ``from_json_string`` returns an object
        (Python data structure) represented by a JSON string
    """
    return json.loads(s_my_list)
