#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for keys, values in new_dic.items():
        new_dic[keys] = values * 2
    return new_dic
