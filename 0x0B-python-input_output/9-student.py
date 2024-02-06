#!/usr/bin/python3
"""student class module"""


class Student:
    """simple student class"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method to return a dictionary representation"""
        return self.__dict__
