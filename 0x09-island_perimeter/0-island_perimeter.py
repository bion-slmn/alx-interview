#!/usr/bin/python3
'''
module to calculate the island perimeter
'''


def island_perimeter(grid):
    '''
    function to calculate the island perimeter
    '''
    perimeter = 0

    for row, row_item in enumerate(grid):
        for col, col_item in enumerate(row_item):
            square_perimeter = 4
            if grid[row][col] == 1:

                # left side
                if col > 0 and grid[row][col - 1] == 1:
                    square_perimeter -= 1

                # right
                if col < len(row_item) - 1 and grid[row][col + 1] == 1:
                    square_perimeter -= 1

                # up side
                if row > 0 and grid[row - 1][col] == 1:
                    square_perimeter -= 1

                # down side
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    square_perimeter -= 1
                perimeter += square_perimeter

    return perimeter
