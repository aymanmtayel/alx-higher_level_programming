#!/usr/bin/python3
"""check inheritance module"""


def is_kind_of_class(obj, a_class):
    """function that checks if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class

    Args:
        obj: to be checked
        a_class: to be checked against

    Returns:
        True: if it is an instance of class or inhertied a type
        False: if otherwise
    """
    return isinstance(obj, a_class)
