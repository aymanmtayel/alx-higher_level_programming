#!/usr/bin/python3
"""print a square module"""


def print_square(size):
    """function to print the square using # symbol

    Args:
        size: length of the square

    Raises:
        TypeError: if size if not integer or is a float and less than 0
        ValueError: if size is less than 0
    """
    if (not isinstance(size, int)) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        print("#" * size)
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
