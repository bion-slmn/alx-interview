#!/usr/bin/python3
''' defines function to solve the n queens challenge using backtracking'''
import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    N = int(sys.argv[1])
except Exception as e:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    '''check if a row and its left and right diagonals are safe to place
    a queen with out it being attacked'''

    # check the row are safe
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check upper diagonal on left side
    for r, c in zip(reversed(range(row)), reversed(range(col))):
        if board[r][c] == 1:
            return False

    # check upper diagonal onthe right side
    for r, c in zip(range(row, N, 1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    return True


def solveNQ_util(result, board, col):
    ''' utility function to solve the N queens challege'''
    if col >= N:
        result.append([row[:] for row in board])
        return

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            solveNQ_util(result, board, col + 1)

            board[row][col] = 0


def solveNQ():
    '''solve  N queen challenge'''
    result = []
    board = [["." for _ in range(N)] for _ in range(N)]
    col = 0
    solveNQ_util(result, board, col)

    for nested_list in result:
        cordinates = []
        for j, sublist in enumerate(nested_list):
            for k, element in enumerate(sublist):
                if element == 1:
                    cordinates.append([j, k])
        print(cordinates)


solveNQ()
