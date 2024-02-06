#!/usr/bin/python3
"""student class module"""


class Student:
    """simple student class"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method to return a dictionary representation"""
        if attrs is None or not type(attrs) is not str:
            return self.__dict__
        dic = {}
        for item in attrs:
            if hasattr(self, item):
                dic.update({item: getattr(self, item)})
        return dic
