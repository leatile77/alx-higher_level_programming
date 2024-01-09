#!/usr/bin/python3
"""Defines pascals triangle function."""
def pascal_triangle(n):
    """Pascal's triangle function.
    Args:
    n (int): size of triangle
    Return:
    list of lists of ints representing pascals triangle
    """
    if n < 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        tmp = [1]
        for i in range(len(tria) - 1):
            tmp.append(tria[i] + tria[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
        
