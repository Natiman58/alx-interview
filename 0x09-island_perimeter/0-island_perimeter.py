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
    perimeter = 0
    if type(grid) != list:
        return 0
    # i -> row , j -> col
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if its a single island increase perimeter by 4
            if grid[i][j] == 1:
                perimeter += 4
                # below = grid[i + 1][j], right = grid[i][j + 1]
                left = grid[i][j - 1]
                top = grid[i - 1][j]

                # check if there is an island to the left of the current island
                if j > 0 and left == 1:
                    perimeter -= 2
                # the check if there is an island on top of the current island
                if j > 0 and top == 1:
                    perimeter -= 2
    return perimeter
