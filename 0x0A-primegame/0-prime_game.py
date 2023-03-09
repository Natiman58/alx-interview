#!/usr/bin/python3
"""
    A script that simulates a game of primes
"""

import random


def sieve(n):
    """ return prime numbers arrray 'primes' using
        sieve of eratosthenes method
    """
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(2, n+1) if primes[i]]


def choose_prime(primes):
    return random.choice(primes)


def remove_multiples(primes, prime):
    if prime not in primes:
        return primes
    for i in range(len(primes)):
        if primes[i] % prime == 0:
            primes[i] = 0
    return [p for p in primes if p != 0]


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = sieve(n)
        maria_turn = True
        while primes:
            if maria_turn:
                prime = choose_prime(primes)
                maria_turn = False
                # print("Maria chooses:", prime)
            else:
                prime = choose_prime(primes)
                maria_turn = True
                # print("Ben chooses:", prime)
            primes = remove_multiples(primes, prime)
            # print("Current state:", primes)
        if maria_turn:
            ben_wins += 1
            # print("Ben wins!")
        else:
            maria_wins += 1
            # print("Maria wins!")
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
