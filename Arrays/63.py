"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
from collections import deque

def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0
    def check_cond(x, y):
        nonlocal obstacleGrid

        if x >= 0 and x < len(obstacleGrid) and y >=0 and y < len(obstacleGrid[0]) and obstacleGrid[x][y] != 1:
            return True
        return False
    queue = deque([(0, 0, set())], )
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = 0
    if obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] != '1':
        obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] = 'X'
    while queue:
        n = len(queue)
        x, y, visited = queue.popleft()
        if obstacleGrid[x][y] == 'X':
            print(visited, end='\n')
            count += 1
            continue
        elif (x, y) in visited:
            continue
        else:
            visited.add((x, y))
            for each_dir in directions:
                if check_cond(x + each_dir[0], y + each_dir[1]):
                    queue.append((x + each_dir[0], y + each_dir[1], visited))
    return count

# O(m*n) space
# def uniquePathsWithObstacles1(self, obstacleGrid):
#     if not obstacleGrid:
#         return
#     r, c = len(obstacleGrid), len(obstacleGrid[0])
#     dp = [[0 for _ in range(c)] for _ in range(r)]
#     dp[0][0] = 1 - obstacleGrid[0][0]
#     for i in range(1, r):
#         dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
#     for i in range(1, c):
#         dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
#     for i in range(1, r):
#         for j in range(1, c):
#             dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
#     return dp[-1][-1]
#
# # O(n) space
# def uniquePathsWithObstacles2(self, obstacleGrid):
#     if not obstacleGrid:
#         return
#     r, c = len(obstacleGrid), len(obstacleGrid[0])
#     cur = [0] * c
#     cur[0] = 1 - obstacleGrid[0][0]
#     for i in range(1, c):
#         cur[i] = cur[i-1] * (1 - obstacleGrid[0][i])
#     for i in range(1, r):
#         cur[0] *= (1 - obstacleGrid[i][0])
#         for j in range(1, c):
#             cur[j] = (cur[j-1] + cur[j]) * (1 - obstacleGrid[i][j])
#     return cur[-1]
#
# # in place
# def uniquePathsWithObstacles(obstacleGrid):
#     if not obstacleGrid:
#         return
#     r, c = len(obstacleGrid), len(obstacleGrid[0])
#     obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
#     for i in range(1, r):
#         obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
#     for i in range(1, c):
#         obstacleGrid[0][i] = obstacleGrid[0][i-1] * (1 - obstacleGrid[0][i])
#     for i in range(1, r):
#         for j in range(1, c):
#             obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
#     return obstacleGrid[-1][-1]
#
# grid = [[0,0,0],
#         [0,1,0],
#         [0,1,0]]
# grid2 = [[1]]
# grid3 = [[0, 0]]
# grid4 = [[0]]
# grid5 = [[0,0,0,0],
#          [0,1,0,0],
#          [0,0,0,0],
#          [0,0,1,0],
#          [0,0,0,0]] # output = 7
#
# print(uniquePathsWithObstacles(grid))
# print(uniquePathsWithObstacles(grid2))
# print(uniquePathsWithObstacles(grid3))
# print(uniquePathsWithObstacles(grid4))
# print(uniquePathsWithObstacles(grid5))
