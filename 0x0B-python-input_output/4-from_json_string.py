#!/usr/bin/python3
"""JSON converter module """
import json


def from_json_string(my_str):
    """function that returns a python object represented by a JSON string"""
    return json.loads(my_str)
