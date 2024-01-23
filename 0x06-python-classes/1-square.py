#!/usr/bin/python3
""" Square Module"""


class Square:
    """A class for a square

    Attributes:
        __size (int): the size of the square
    """

    def __init__(self, size):
        """initializes an instance of sqaure class

        Args:
            size (int): length of any side of the square.
        """
        self.__size = size
