#!/usr/bin/python3
"""Module that defines a Pascal's triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle

    Args:
        n: number of rows in the triangle

    Returns:
        List of lists representing Pascal's triangle, or empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
