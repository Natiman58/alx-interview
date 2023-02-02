#!/usr/bin/python3
"""
    A module that solves the N-queen problem
    The N queens puzzle is the challenge of placing
    N non-attacking queens on an N×N chessboard.
    Write a program that solves the N queens problem.
"""
from sys import argv

N = int(argv[1])

# chessboard
# NXN matrix with all elements 0
board = [[0]*N for _ in range(N)]


def is_attack(i, j):
    """
        Checks if the queen at (i, j) is attacked by another queen
        :param i: the row of the queen
        :param j: the column of the queen
    """
    # check if there is a queen in row or column
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # checking the diagonals
    for k in range(0, N):
        for _l in range(0, N):
            if (k+_l == i+j) or (k-_l == i-j):
                if board[k][_l] == 1:
                    return True
    return False


def N_queen(n):
    """
        check the num of queens
    """
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not is_attack(i, j) and board[i][j] != 1):
                board[i][j] = 1
                if N_queen(n-1):
                    return True
                board[i][j] = 0
    return False


N_queen(N)

idx_list = []
for row in (board):
    row_idx = board.index(row)
    for col in row:
        col_idx = row.index(col)
        if col == 1:
            idx_list.append([row_idx, col_idx])
print(idx_list)
# print(board)
