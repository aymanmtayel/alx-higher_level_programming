#!/usr/bin/python3
"""sub class module"""


def inherits_from(obj, a_class):
    """function that checks if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: to be checked
        a_class: to be checked against

    Returns:
        True: is pass
        False: if otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
