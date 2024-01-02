#!/usr/bin/python3
def uppercase(str):
    length = len(str) - 1
    for i in range(len(str)):
        if 96 < ord(str[i]) < 122:
            print(f"{chr(ord(str[i]) - 32)}", end="" if i < length else "\n")
        else:
            print(str[i], end="")
