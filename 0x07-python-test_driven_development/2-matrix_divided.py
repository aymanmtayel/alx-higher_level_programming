#!/usr/bin/python3
""" Dvide Matrix Module """


def matrix_divided(matrix, div):
    """function to divide all the elements of a matrix by a divisour

    Args:
        matrix: List containing int or float
        div: divsour to be divided by
    Return:
        list containing the elements after division
    Raises:
        TypeError: if matrix is not list containing int or float
        TypeError: if size mismatch
        TypeError: if div is not int or float
        ZeroDivision Error: if div is zero
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if not isinstance(i, list) or len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
    return [[round(j / div, 2) for j in i] for i in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
