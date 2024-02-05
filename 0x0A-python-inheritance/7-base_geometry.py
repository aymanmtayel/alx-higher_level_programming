#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """ a class BaseGeometry"""
    def area(self):
        """function to calculate the area (not implemented yet)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validating the value

        Args:
            name: the variable name
            value: it value to be checked

        Raises:
            TypeError: if it is not integer
            Value error: if less than of equal 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
