#!/usr/bin/python3
"""
    A method that calculates the minimum number of operations
    to result n number of H characters from a text file
"""


def minOperations(n):
    """
        Returns the minimum number of operations
    """
    if not isinstance(n, int):   # return 0 if n is not int
        return 0

    count = 0    # operation counter
    min_op = 2   # minimum number of operations initially
    while n > 1:  # starts with the smallest even or odd number n
        while (n % min_op == 0):  # if n is even min_op is always 2(c-p)
            count = count + min_op  # increase the op count by 2
            n = n / min_op   # the remaining nums become halved loop...
        min_op = min_op + 1  # if n is odd the min_op is always 3(c-p-p) loop..

    return count
