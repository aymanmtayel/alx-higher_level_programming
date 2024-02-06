#!/usr/bin/python3
"""create an object module"""
import json


def load_from_json_file(filename):
    """function to create an object from JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
