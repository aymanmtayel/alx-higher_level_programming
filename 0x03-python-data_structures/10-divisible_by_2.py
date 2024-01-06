#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    length = len(my_list)
    if my_list is None:
        return None
    else:
        for k in range(length - 1):
            if my_list[k] % 2 == 0:
                result.append(True)
            else:
                result.append(False)
    return result
