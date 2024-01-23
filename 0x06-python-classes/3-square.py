#!/usr/bin/python3
""" Square Module"""


class Square:
    """A class for a square

    Attributes:
        __size (int): the size of the square
    """

    def __init__(self, size=0):
        """initializes an instance of sqaure class

        Args:
            size (int): length of any side of the square.
        Raises:
            TypeError: if (size) not an integer
            ValueError: f size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """public instace method area the returns the current square area"""
        return self.__size ** 2
