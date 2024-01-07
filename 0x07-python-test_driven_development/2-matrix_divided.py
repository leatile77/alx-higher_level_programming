#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """
    Args:
    matrix (list): List of lists of float or int elements
    div (int/float): The divisor

    Raises:
    TypeError: matrix(list of lists) contains non-int/float
    TypeError: matrix rows have different sizes
    TypeError: divisor is 0

    Return:
    A new matrix with divided elements
    """

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if (not all(isinstance(row, list) for row in matrix) or not all((isinstance(elem, int) or isinstance(elem, float)) for elem in [values for row in matrix for values in row])):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by 0")

    new_list = ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

    return (new_list)
