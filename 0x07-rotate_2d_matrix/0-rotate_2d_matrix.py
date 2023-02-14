#!/usr/bin/python3
"""
    A simple script that rotates a 2D matrix
    90° clockwise
"""


def rotate_2d_matrix(matrix):
    # Get the number of rows in the matrix
    n = len(matrix)

    # Loop through each layer of the matrix,
    # starting from the outermost layer and working inward
    # loop through only the half of the row and column layers
    for i in range(n // 2):
        # Loop through each cell in the current layer
        for j in range(i, n - i - 1):
            # Save the top cell's value in a temporary variable
            temp = matrix[i][j]

            # Move the left cell's value to the top cell
            matrix[i][j] = matrix[n - j - 1][i]

            # Move the bottom cell's value to the left cell
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]

            # Move the right cell's value to the bottom cell
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

            # Move the top cell's saved value to the right cell
            matrix[j][n - i - 1] = temp
