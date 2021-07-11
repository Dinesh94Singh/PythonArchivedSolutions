"""
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
 """

from collections import deque

class Solution:
    def zombie_in_matrix(self, grid):
        def getRottenIndices():
            nonlocal grid, d
            rotten_indices = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        rotten_indices.append((i, j, d))  # 0 for the time taken
            return rotten_indices

        def check_cond(i, j):
            nonlocal grid
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 0:
                grid[i][j] = 1
                return True
            return False

        d = 0
        queue = deque(getRottenIndices())
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y, d = queue.popleft()
            for each_dir in directions:
                if check_cond(x+each_dir[0], y+each_dir[1]):
                    queue.append((x+each_dir[0], y+each_dir[1], d + 1))

        if any(0 in row for row in grid):
            return -1
        return d

grid = [[0, 1, 1, 0, 1],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0]]

s = Solution()

s.zombie_in_matrix(grid)
