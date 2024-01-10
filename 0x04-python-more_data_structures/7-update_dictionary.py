#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for keys, values in a_dictionary.items():
        if keys == key:
            a_dictionary[key] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
