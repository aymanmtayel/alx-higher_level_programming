#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    else:
        for i in my_list:
            for k in my_list:
                if k > i:
                    i = k
                    continue
    return i
