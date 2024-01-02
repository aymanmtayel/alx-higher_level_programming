#!/usr/bin/python3
def islower(str):
    if ord(str) >= ord('a') and ord(str) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    for char in str:
        if islower(char):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
