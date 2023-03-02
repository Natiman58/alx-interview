#!/usr/bin/python3
"""
    calculate the perimeter of an island
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island.

    Args:
        grid (List[List[int]]): A rectangular grid of
        integers representing an island.
        0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.

    """
    height = len(grid)
    width = len(grid[0])
    perimeter = 0
    # i -> row, j -> col
    for i in range(height):
        for j in range(width):
            top = grid[i - 1][j]
            left = grid[i][j - 1]
            # if there is an island incresese perimeter by 4
            if grid[i][j] == 1:
                perimeter += 4
                # check the adjacent islands(top and left)
                # and subtract 2(the walls that dont contribute to Perimeterx)
                if i > 0 and top == 1:
                    perimeter -= 2
                if j > 0 and left == 1:
                    perimeter -= 2
    return perimeter
