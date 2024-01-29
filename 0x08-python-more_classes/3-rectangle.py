#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Define a rectangle class"""
    def __init__(self, width=0, height=0):
        """rectangle initialized"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter function to get the private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """function to set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """function to get the private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """function to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """returns the printed rectangle"""
        printed = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(0, self.__height):
                printed += "#" * self.__width
                if i < self.__height - 1:
                    printed += "\n"
        return printed
