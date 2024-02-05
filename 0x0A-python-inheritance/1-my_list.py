#!/usr/bin/python3
"""Inheritance module"""


class MyList(list):
    """list class to be sorted"""
    def print_sorted(self):
        """method that print the list sorted"""
        print(sorted(self))
