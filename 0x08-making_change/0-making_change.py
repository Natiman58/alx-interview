#!/usr/bin/python3
"""
    A script that calculates changes of a coin using dynamic programming
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
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

    # then start from the second coin val
    for i in range(1, total + 1):
        for coin in coins:  # iterate through each coin
            if coin <= i:  # if each coin is < total
                # get the min amount by checking the current & prev coin val
                min_amount_coin = min(min_coin[i], min_coin[i - coin] + 1)
                # update the min coin list
                min_coin[i] = min_amount_coin

    return min_coin[total] if min_coin[total] != float('inf') else -1
