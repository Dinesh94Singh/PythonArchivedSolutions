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
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0]) - 1, -1, -1):
            if i == len(grid) - 1 and j != len(grid[0]) - 1:
                # 4, 2 on the last row
                grid[i][j] = grid[i][j] + grid[i][j + 1]
            elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                # 1, 1 on the last column
                grid[i][j] = grid[i][j] + grid[i + 1][j]
            elif j != len(grid[0]) - 1 and i != len(grid) - 1:
                grid[i][j] = min(grid[i + 1][j], grid[i][j + 1]) + grid[i][j]
    return grid[0][0]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

# minPathSum(grid)

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(row, col, path):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                # total = sum([grid[each[0]][each[1]] for each in path])
                total_sum = 0
                for r, c in path:
                    total_sum += grid[r][c]

                self.ans = min(self.ans, total_sum)
                return

            visited.add((row, col))

            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= r <= len(grid) - 1 and 0 <= c <= len(grid[0]) - 1 and (r, c) not in visited:
                    dfs(r, c, path + [(r, c)])

            visited.remove((row, col))

        visited = set()

        self.ans = float('inf')

        dfs(0, 0, [(0, 0)])
        return self.ans

s = Solution()
print(s.minPathSum(grid))