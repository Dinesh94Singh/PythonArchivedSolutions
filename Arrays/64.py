'''
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

# def minPathSum(self, grid: List[List[int]]) -> int:
def minPathSum(grid):
  for i in range(len(grid)-1, -1, -1):
    for j in range(len(grid[0])-1, -1, -1):
      if  i == len(grid) - 1 and j != len(grid[0]) - 1:
        # 4, 2 on the last row
        grid[i][j] = grid[i][j] + grid[i][j+1]
      elif j == len(grid[0]) - 1 and i != len(grid) - 1:
        # 1, 1 on the last column
        grid[i][j] = grid[i][j] + grid[i+1][j]
      elif j != len(grid[0]) - 1 and i != len(grid) -1:
        grid[i][j] = min(grid[i+1][j], grid[i][j+1]) + grid[i][j]
  return grid[0][0]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

minPathSum(grid)