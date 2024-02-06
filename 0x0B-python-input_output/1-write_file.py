#!/usr/bin/python3
"""Write a string to a text file module"""


def write_file(filename="", text=""):
    """function to write to a filename a given string

    Args:
        filename: the filename to be created or write inside it
        text: the string to be written inside the file

    Returns: the number of characters written
    """
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
