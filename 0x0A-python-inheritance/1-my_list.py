#!/usr/bin/python3
"""Inheritance module"""


class MyList(list):
    """My list class that has only one method (sort)"""
    def print_sorted(self):
        """method that print the list sorted"""
        print(sorted(self))
