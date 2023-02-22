#!/usr/bin/python3
"""
    A script that calculates changes of a coin using dynamic programming
"""

def makeChange(coins, total):
    """
        returns the minimun no of coins needed to make the total
        args:
            coins: list of different coins of different values
            total: the total required
    """
    # create an empty list that keeps track of the min num of coins needed
    # start by an intital value of unknown data set; infity
    # and length of total + 1
    min_coin = [float('inf')] * (total + 1)

    # set the first value 0
    min_coin[0] = 0

    # Iterate through each coin and update the min_coin array
    for coin in coins:
        for i in range(coin, total + 1):
            if min_coin[i - coin] != float('inf'):
                min_coin[i] = min(min_coin[i], min_coin[i - coin] + 1)

    # If it's not possible to make the total with the given coins, return -1
    if min_coin[total] == float('inf'):
        return -1

    return min_coin[total]
