#!/usr/bin/python3
"""
    script that adds all arguments to a Python list,
    and then save them to a file
"""
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


l_args = len(sys.argv)

if not os.path.isfile("add_item.json"):
    with open("add_item.json", "w", encoding="utf-8") as f:
        f.write("[]")

if l_args > 1:
    data = load_from_json_file("add_item.json")
    for i in range(1, l_args):
        data. append(sys.argv[i])
    save_to_json_file(data, "add_item.json")
