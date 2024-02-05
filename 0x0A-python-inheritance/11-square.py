#!/usr/bin/python3
"""Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass inherited from Rectangle"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method to calculate the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """user friendly representation for the class square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
