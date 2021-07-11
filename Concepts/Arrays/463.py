"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

def islandPerimeter(grid):
    def dfs(r, c):
        nonlocal grid
        if 0 <= r < len(grid) and 0 <= c < len(grid[1]) and grid[r][c] == -1:
            return 0
        elif 0 <= r < len(grid) and 0 <= c < len(grid[1]) and grid[r][c] == 1:
            grid[r][c] = -1
            return dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        else:
            return 1

    row, col = len(grid), len(grid[0])
    peri = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                peri = dfs(i, j)
    return peri

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

islandPerimeter(grid)
