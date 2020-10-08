#!/usr/bin/python3
"""module space"""


from sys import argv
save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file

try:
    obj = load("add_item.json")
except:
    obj = []
obj += argv[1:]
save(obj, "add_item.json")
