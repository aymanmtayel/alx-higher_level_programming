#!/usr/bin/python3
"""this is the append to file module"""


def append_write(filename="", text=""):
    """function to create a file and append a text to it

    Args:
        filename: the file to be created or append to it
        text: the text to be appended

    Returns: the number of character appended or added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
