#!/usr/bin/python3
"""module to find a peak"""


def find_peak(list_of_integers):
    """function to find the peak of a list of integers"""
    if not list_of_integers:
        return None
    curr = 0
    last = len(list_of_integers) - 1

    while curr < last:
        half = (curr + last) // 2
        if list_of_integers[half] < list_of_integers[half + 1]:
            curr = half + 1
        else:
            last = half
    return list_of_integers[curr]
