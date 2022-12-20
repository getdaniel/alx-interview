#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Implements the pascal triangle."""
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for index in range(n):
        line = []
        for jndex in range(index + 1):
            if jndex == 0 or jndex == index:
                line.append(1)
            elif index > 0 and jndex > 0:
                line.append(triangle[index - 1][jndex - 1] +
                            triangle[index - 1][jndex])
        triangle.append(line)
    return triangle
