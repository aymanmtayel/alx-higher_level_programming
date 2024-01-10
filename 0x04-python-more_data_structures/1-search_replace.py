#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i, value in enumerate(my_list):
        if value == search:
            my_list[i] = replace
    return my_list
