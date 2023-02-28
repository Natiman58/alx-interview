#!/usr/bin/python3
"""
    calculate the perimeter of an island
"""
from typing import List


def island_perimeter(grid):
    """
        grid: collection of islands
        return: their perimeter
    """
    new_arr = []
    for i in range(len(grid)):
        for j in range(i + 1):
            if grid[i][j] == 1:
                new_arr.append(grid[i][j])
    return (len(new_arr) * 4) - (2 * len(new_arr) - 2)
