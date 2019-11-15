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

"""
This solution is failing for - [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
"""


def uniquePathsWithObstacles(obstacle_grid):
    if obstacle_grid[0][0] == 1:
        return 0

    def check_cond(x, y):
        nonlocal obstacle_grid

        if 0 <= x < len(obstacle_grid) and 0 <= y < len(obstacle_grid[0]) and obstacle_grid[x][y] != 1:
            return True
        return False

    queue = deque([(0, 0, set())], )
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = 0
    print('last element is - ', obstacle_grid[len(obstacle_grid) - 1][len(obstacle_grid[0]) - 1])
    if obstacle_grid[len(obstacle_grid) - 1][len(obstacle_grid[0]) - 1] != 1:
        obstacle_grid[len(obstacle_grid) - 1][len(obstacle_grid[0]) - 1] = 'X'  # End point
    else:
        return 0  # no end point
    while queue:
        n = len(queue)
        x, y, visited = queue.popleft()
        if obstacle_grid[x][y] == 'X':
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
def uniquePathsWithObstacles1(obstacle_grid):
    if not obstacle_grid:
        return
    r, c = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0] = 1 - obstacle_grid[0][0]  # if 1 => Mark it 0, if 0 -> Mark it 1
    for i in range(1, r):
        dp[i][0] = dp[i - 1][0] * (1 - obstacle_grid[i][0]) # First col -> any blockages -> if so, mark them and its
        # effecting grid elements as 0
    for i in range(1, c):
        dp[0][i] = dp[0][i - 1] * (1 - obstacle_grid[0][i]) # First row -> any blockages -> if so, mark them and its
        # effecting grid elements as 0

    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (1 - obstacle_grid[i][j])
    return dp[-1][-1]


# O(n) space
def uniquePathsWithObstacles2(obstacle_grid):
    if not obstacle_grid:
        return
    r, c = len(obstacle_grid), len(obstacle_grid[0])
    cur = [0] * c
    cur[0] = 1 - obstacle_grid[0][0]
    for i in range(1, c):
        cur[i] = cur[i - 1] * (1 - obstacle_grid[0][i])
    for i in range(1, r):
        cur[0] *= (1 - obstacle_grid[i][0])
        for j in range(1, c):
            cur[j] = (cur[j - 1] + cur[j]) * (1 - obstacle_grid[i][j])
    return cur[-1]


# in place
def uniquePathsWithObstacles(obstacle_grid):
    if not obstacle_grid:
        return
    r, c = len(obstacle_grid), len(obstacle_grid[0])
    obstacle_grid[0][0] = 1 - obstacle_grid[0][0]
    for i in range(1, r):
        obstacle_grid[i][0] = obstacle_grid[i-1][0] * (1 - obstacle_grid[i][0])
    for i in range(1, c):
        obstacle_grid[0][i] = obstacle_grid[0][i-1] * (1 - obstacle_grid[0][i])
    for i in range(1, r):
        for j in range(1, c):
            obstacle_grid[i][j] = (obstacle_grid[i-1][j] + obstacle_grid[i][j-1]) * (1 - obstacle_grid[i][j])
    return obstacle_grid[-1][-1]
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

grid6 = [[0, 1]]

print(uniquePathsWithObstacles(grid6))
