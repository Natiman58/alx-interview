#!/usr/bin/python3
"""
    calculate the perimeter of an island
"""


def island_perimeter(grid):
    """
        grid: collection of islands
        return: their perimeter
    """
    perimeter = 0
    # i -> row , j -> col
    for i in range(len(grid)):
        for j in range(i + 1):
            # if its a single island increase perimeter by 4
            if grid[i][j] == 1:
                perimeter += 4
                # if the is an island infront of the current island
                if grid[i - 1][j] == 0 and grid[i + 1][j] == 1 and grid[i][j + 1] == 0 and grid[i][j - 1] == 0:
                    perimeter -= 2
                # if there is's between islands(front and back)
                if grid[i - 1][j] == 1 and grid[i + 1][j] == 1 and grid[i][j + 1] == 0 and grid[i][j - 1] == 0:
                    perimeter += 2
                # if there is an island in the back and on the right
                if grid[i - 1][j] == 1 and grid[i + 1][j] == 0 and grid[i][ j + 1] == 1 and grid[i][j - 1] == 0:
                    perimeter -= 4
                # if there are islands on the back and left
                if grid[i - 1][j] == 1 and grid[i + 1][j] == 0 and grid[i][ j + 1] == 0 and grid[i][j - 1] == 1:
                    perimeter -= 4
                # if in betweeen island (left and right)
                if grid[i - 1][j] == 0 and grid[i + 1][j] == 0 and grid[i][ j + 1] == 1 and grid[i][j - 1] == 1:
                    perimeter -= 4
    return perimeter

                    