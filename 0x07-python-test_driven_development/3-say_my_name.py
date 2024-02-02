#!/usr/bin/python3
"""Say my name module """


def say_my_name(first_name, last_name=""):
    """say my name function

    Args:
        first_name: first name to be printed
        last_name: last name to be printed
    Raises:
        TypeError: if first name or last name were not strings
    """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
