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
        """
        self.__size = size

    @property
    def size(self):
        """property to get the value of the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """property to set the value of the size of the square

        Raises:
            TypeError: if (size) not an integer
            ValueError: f size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public instace method area the returns the current square area"""
        return self.__size ** 2
