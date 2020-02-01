"""

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3



"""


def num_of_islands_dfs(grid):
    def dfs(row, col):
        nonlocal grid, rc, cc

        if row < 0 or row >= rc or col < 0 or col >= cc:
            return
        if grid[row][col] == 1:
            grid[row][col] = 0  # if not, this will enter into a cycle.
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

    if not grid or len(grid) == 0:
        return
    total_no_of_islands = 0
    rc = len(grid)
    cc = len(grid[0])
    for r in range(rc):
        for c in range(cc):
            if grid[r][c] == 1:
                print(grid)
                total_no_of_islands += 1
                dfs(r, c)
    return total_no_of_islands


grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
grid2 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
num_of_islands_dfs(grid2)
