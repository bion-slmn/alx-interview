#!/usr/bin/python3
'''calculating the minimum number of operation of copy_all and paste to
reach N'''


def minOperations(n: int) ->int:
    '''calcutating minoperation'''

    if n <= 1:
        return 0
    if n == 2:
        return 2
    

    clipBoard = 'H'
    val = 'HH'
    remaining = 0
    counter = 2

    for x in range(n):
        if len(val) == n:
            return counter
        # when to copy and paste
        remaining = n - len(val)
        if remaining % len(val) == 0:
            clipBoard = val
            val += clipBoard
            counter += 2
        else:
            val += clipBoard
            counter += 1
