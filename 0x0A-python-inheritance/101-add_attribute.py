#!/usr/bin/python3
"""Function to add attributes to an object"""


def add_attribute(obj, attrib, value):
    """ function to add new attribute if it is doable

    Args:
        obj: the object to add the attribute to it
        attrib: the name of the attribute to be added
        value: the value of the attribute

    Raises:
        TypeError: if the attribute can't be added to the object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attrib, value)
