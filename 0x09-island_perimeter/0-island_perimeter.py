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
                back = grid[i - 1][j]
                front = grid[i + 1][j]
                left = grid[i][j - 1]
                right = grid[i][j + 1]

                # if there is an island infront of the current island
                if back == 0 and front == 1 and right == 0 and left == 0:
                    # print(perimeter)
                    perimeter += 2
                    # print(perimeter)
                # if is's between islands(front and back)
                elif back == 1 and front == 1 and right == 0 and left == 0:
                    perimeter -= 2
                    # print(perimeter)
                # if there is an island in the back and on the right
                elif back == 1 and front == 0 and right == 1 and left == 0:
                    # print(perimeter)
                    perimeter -= 4
                    # print(perimeter)

                # if there are islands on the back and left
                elif back == 1 and front == 0 and right == 0 and left == 1:
                    perimeter += 0
                    # print(perimeter)
                # if in betweeen island (left and right)
                elif back == 0 and front == 0 and right == 1 and left == 1:
                    perimeter -= 0
                    # print(perimeter)
    return perimeter - 4
