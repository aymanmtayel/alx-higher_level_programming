#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        square_row = [x ** 2 for x in row]
        squared_matrix.append(square_row)
    return squared_matrix
