#!/usr/bin/python3
"""module space"""
import json


def from_json_string(my_str):
    """ returns an object (Python data structure) represented by a JSON"""

    return json.loads(my_str)
