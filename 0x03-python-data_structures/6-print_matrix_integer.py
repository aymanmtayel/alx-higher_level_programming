#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for i in matrix:
            if len(i) == 0:
                print()
            for k, num in enumerate(i):
                if k == len(i) - 1:
                    print("{:d}".format(num), end='\n')
                else:
                    print("{:d}".format(num), end=" ")
