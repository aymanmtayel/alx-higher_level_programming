#!/usr/bin/python3
"""List module"""


def lookup(obj):
    """function that returns the list of available attributes
    and method of an object

    Args:
        obj: object to be listed

    Returns: list of available attributes and methods of an object:
    """
    return (dir(obj))
