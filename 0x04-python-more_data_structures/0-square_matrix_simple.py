#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for row in matrix:
        sqd = map(lambda x: x**2, row)
        squared.append(list(sqd))
    return squared
