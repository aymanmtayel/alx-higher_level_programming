#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    total = 0
    roman_dic = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    total = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0
    for char in reversed(roman_string):
        result = roman_dic[char]
        total += result if total < result * 5 else -result
    return int(total)
