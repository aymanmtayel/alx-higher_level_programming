#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = 23232
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMCDXXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCLXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
