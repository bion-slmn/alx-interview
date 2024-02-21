#!/usr/bin/python3
'''module to define a function that rotates a 2d matrix'''


def rotate_2d_matrix(matrix):
    '''
    rotate nxn  2d matrix by 90 degree clockwise in place
    '''
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
