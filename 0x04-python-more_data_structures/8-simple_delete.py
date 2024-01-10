#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys, values in a_dictionary.items():
        if keys == key:
            del a_dictionary[key]
            return a_dictionary
    return a_dictionary
