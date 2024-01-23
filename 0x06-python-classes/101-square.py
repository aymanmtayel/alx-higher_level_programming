#!/usr/bin/python3
""" Square Module"""


class Square:
    """A class for a square

    Attributes:
        __size (int): the size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes an instance of sqaure class

        Args:
            size (int): length of any side of the square.
            position (int, int): the position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """property to get the value of the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """public instace method area the returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """public instance method to print the square using #"""
        if self.__size == 0:
            print()
            return

        for _ in range(0, self.__position[1]):
            print()
        for _ in range(0, self.__size):
            for _ in range(0, self.__position[0]):
                print(" ", end="")
            for _ in range(0, self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """public instance method to print the square using #"""
        if self.__size == 0:
            print()
            return ""

        printed = ""
        for _ in range(0, self.__position[1]):
            printed += "\n"
        for _ in range(0, self.__size):
            for _ in range(0, self.__position[0]):
                printed += " "
            for _ in range(0, self.__size):
                printed += "#"
            printed += "\n"

        return printed.strip()
