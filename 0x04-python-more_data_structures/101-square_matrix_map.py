#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda sqrd: list(map(lambda x: x**2, sqrd)), matrix))
