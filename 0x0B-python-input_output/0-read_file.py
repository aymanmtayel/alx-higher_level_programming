#!/usr/bin/python3
"""Read a file module"""


def read_file(filename=""):
    """function to read a file and print its content to stdout

        Args:
            filename: the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data, end='')
