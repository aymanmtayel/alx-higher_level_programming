#!/usr/bin/python3
"""module for a rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ a subclass of BaseGeometry for a rectangle"""
    def __init__(self, width, height):
        """constructor requiring width and height and validate them
        from the parent class function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method to calculate the area and return it"""
        return self.__width * self.__height

    def __str__(self):
        """return user friendly representation of the object"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
