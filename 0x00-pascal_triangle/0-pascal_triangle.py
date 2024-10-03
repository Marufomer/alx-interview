#!/usr/bin/python3
"""
Pascal's Triangle
"""
from math import factorial;


def pascal_triangle(rows):
    """
    Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
    """

    result = [] # collection of arry
    if rows > 0: # Returns an empty list if n <= 0
        def combine(n, r):
            return int((factorial(n))/(factorial(r)*factorial(n-r))) # calculate element of row

        for i in range(rows):
            row = [] # element of row 

            for j in range(i + 1):
                row.append(combine(i,j))
            result.append(row)
    return result
