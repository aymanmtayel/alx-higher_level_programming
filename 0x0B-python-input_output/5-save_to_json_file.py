#!/usr/bin/python3
"""write a JSON string module """
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: object to be wirtten
        filename: the filename to write into
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
