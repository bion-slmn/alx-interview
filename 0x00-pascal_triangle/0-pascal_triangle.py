#!/usr/bin/python3
'''this module answers a pascal triangle question'''


def factorial(n):
    '''this definesa factorial solution for a given number'''
    if n == 0:
        return 1

    return n * factorial(n-1)


def comb(x, y):
    '''defines a combination formulat'''
    a = factorial(x)
    b = factorial(y)
    c = factorial(x - y)

    return a // (b * c)


def pascal_triangle(n):
    ''' returns a list of lists of integers representing
    the Pascal’s triangle of n'''
    matrix = []

    if n <= 0:
        return matrix

    for x in range(n):
        row = []
        for y in range(x + 1):
            result = comb(x, y)
            row.append(result)

        matrix.append(row)

    return matrix
