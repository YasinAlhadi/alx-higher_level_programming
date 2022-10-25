#!/usr/bin/python3
"""
    ``6-load_from_json_file`` module
"""
import json


def load_from_json_file(filename):
    """
        function ``load_from_json_file`` that creates an Object
        from a “JSON file”
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
