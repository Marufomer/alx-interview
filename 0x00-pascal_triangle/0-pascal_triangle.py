#!/usr/bin/python3
"""
Pascal's Triangle
"""
from math import factorial;


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
    """

    result = []
    if n > 0:
        def combine(n, r):
            return int((factorial(n))/(factorial(r)*factorial(n-r)))
        for i in range(n):
            row = [] 
            for j in range(i + 1):
                row.append(combine(i,j))
            result.append(row)
    return result

