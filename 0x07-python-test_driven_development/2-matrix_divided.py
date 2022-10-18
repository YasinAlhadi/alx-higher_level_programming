#!/usr/bin/python3
"""``2-matrix_divided`` module"""


def matrix_divided(matrix, div):
    """
         function that divides all elements of a matrix.
    """
    for row in matrix:
        if len(row) == 0 or type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if any(len(i) != len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    try:
        result = [[round(value / div, 2) for value in row] for row in matrix]
    except TypeError:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    return result
