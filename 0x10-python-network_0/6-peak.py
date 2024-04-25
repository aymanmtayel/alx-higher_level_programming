#!/usr/bin/python3
"""module to find a peak"""


def find_peak(list_of_integers):
    """function to find the peak of a list of integers"""
    if not list_of_integers:
        return None
    mind = None
    for integer in list_of_integers:
        if mind is None or mind < integer:
            mind = integer
    return mind
