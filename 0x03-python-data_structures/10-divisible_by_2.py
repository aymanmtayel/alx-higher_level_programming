#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = [0]
    length = len(my_list)
    for k in range(length - 1):
            if my_list[k] % 2 == 0:
                result.append(True)
            else:
                result.append(False)
    return result
