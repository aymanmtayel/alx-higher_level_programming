#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Define a rectangle class"""

    number_of_instances = 0
    """counter for number of rectangel instances"""

    print_symbol = "#"
    """inital value for print_symbol"""

    def __init__(self, width=0, height=0):
        """rectangle initialized"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                printed += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    printed += "\n"
        return printed

    def __repr__(self):
        """return a representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """detects when an instance has been deleted and print a message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two rectangles

        Args:
            rect_1: the first instance
            rect_2: the second instance
        Raises:
        TypeError: if rect_1 or rect_2 are not instance of rectangle
        Return:
            the larger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2
