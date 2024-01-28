#!/usr/bin/python3
""" Add two integers module """


def add_integer(a, b=98):
    """function to add two integers

    Args:
        a: the first integer or float.
        b: the seconde integer or float, by default it will be 98.

    Raises:
        TypeError: if a, b are not integers or floats.

    Return:
        the sum of the two integers.
    """
    if (isinstance(a, (int, float))) and (isinstance(b, (int, float))):
        return int(a + b)
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
