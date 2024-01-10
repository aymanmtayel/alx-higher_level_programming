#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary.items())
    for key, value in sorted_dic:
        print("{}: {}".format(key, value))
