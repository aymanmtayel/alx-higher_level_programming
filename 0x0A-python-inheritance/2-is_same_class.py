#!/usr/bin/python3
"""test instance module"""


def is_same_class(obj, a_class):
    """function that test if an object is
    exactly an instance of the specified class

    Args:
        obj: object to be tested
        a_class: the class to be tested against

    Returns:
        True: if the object is an instance
        False: if otherwise
    """
    return type(obj) is a_class
