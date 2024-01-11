#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    total = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0
    if roman_string[0] == 'I':
        total = total - 1
        for i in range(1, len(roman_string)):
            if roman_string[i] == 'I':
                total = total - 1
            else:
                total = total + roman_dic.get(roman_string[i])
    else:
        for char in roman_string:
            total = total + roman_dic.get(char)
    return int(total)
