#!/usr/bin/python3
def uppercase(str):
    length = len(str) - 1
    for i in range(len(str)):
        if 96 < ord(str[i]) < 123:
            print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("{}".format(str[i]), end="")
    print("{}".format(""))
