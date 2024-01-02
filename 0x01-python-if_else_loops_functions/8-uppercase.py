#!/usr/bin/python3
def islower(c):
    asci = ord(c)
    if 96 < asci < 123:
        return True
    else:
        return False


def uppercase(str):
    for char in str:
        if char is islower:
            char = chr(ord(i) - 32)
        print("{}".format(char), end="")
    print("")
