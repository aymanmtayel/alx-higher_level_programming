#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    values = sys.argv[0:]
    length = len(sys.argv) - 1
    i = 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:\n1: {}".format(values[0]))
    else:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, values[i]))
