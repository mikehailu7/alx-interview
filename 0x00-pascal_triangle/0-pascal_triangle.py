#!/usr/bin/python3
#Author: MikiasHailu
"""Pascal Triangle"""


def pascal_triangle(n):
    """this is a pascal trinagle 
    represent with n sides"""
    if n <= 0:
        return []

    pascal_t = []

    for m in range(n):
        pascal_t.append([])
        pascal_t[m].append(1)

        for j in range(1, m):
            x = pascal_t[m-1][j-1]
            y = pascal_t[m-1][j]
            pascal_t[m].append(x+y)

        if(n != 0 and m != 0):
            pascal_t[m].append(1)

    return pascal_t
