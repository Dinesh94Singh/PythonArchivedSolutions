'''

62. Unique paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

'''

def uniquePath(m, n):
    # @return an integer
    grid = [[1 for x in range(n)] for x in range(m)]
    print(grid)
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i][j-1] + grid[i-1][j]
    return grid[-1][-1] # last element in the grid

uniquePath(3, 2)