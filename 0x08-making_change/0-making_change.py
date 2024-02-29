#!/usr/bin/python3
'''
making change algorithm
'''
import sys


def minCoinsUtil(coins, m, V, dp):
    if V == 0:
        return 0

    if dp[V] != -1:
        return dp[V]

    res = sys.maxsize

    for i in range(m):
        if coins[i] <= V:
            sub_res = minCoinsUtil(coins, m, V - coins[i], dp)
            if sub_res != sys.maxsize and sub_res + 1:
                res = sub_res + 1
    dp[V] = res
    return res if res != sys.maxsize else -1


def makeChange(coins, total):
    if total == 0:
        return 0

    memo = [-1] * (total + 1)
    m = len(coins)

    return minCoinsUtil(coins, m, total, memo)
