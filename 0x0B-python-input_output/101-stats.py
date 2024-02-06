#!/usr/bin/python3
"""Computer Metrics Module"""
from sys import stdin


codes = {'200': 0,
         '301': 0,
         '400': 0,
         '401': 0,
         '403': 0,
         '404': 0,
         '405': 0,
         '500': 0}
size = 0
indx = 0


def printed():
    """function to print the info"""
    print(f"File size: {size}")
    for key, value in sorted(codes.items()):
        if value > 0:
            print("{:s}: {:d}".format(key, value))


try:
    for lines in stdin:
        split_l = lines.split()
        if len(split_l) >= 2:
            status = split_l[-2]
            size += int(split_l[-1])
            if status in codes:
                codes[status] += 1
        indx += 1
        if indx % 10 == 0:
            printed()
    printed()
except KeyboardInterrupt as exp:
    printed()
