#!/usr/bin/python3
"""script to add arguments to a python list"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])

try:
    loadf = load('add_item.json')
except Exception:
    loadf = []

loadf.extend(args)
save(loadf, 'add_item.json')
