#!/usr/bin/python3
"""JSON representation module"""
import json


def to_json_string(my_obj):
    """function to return the JSON representation of an object

    Args:
        my_obj: the object to be converted

    Returns: the JSON representation
    """
    return json.dumps(my_obj)
