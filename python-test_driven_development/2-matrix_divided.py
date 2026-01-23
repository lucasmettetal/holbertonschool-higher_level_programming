#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.
    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    Returns:
        list of lists of float: A new matrix with the divided values rounded to 2 decimal places.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == float('inf') or div == float('-inf'):
        return [[0.0 for _ in row] for row in matrix]

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, (int, float)) for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
