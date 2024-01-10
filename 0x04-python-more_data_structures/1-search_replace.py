#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda old: replace if old == search else old, my_list))
