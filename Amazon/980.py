"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
"""


class Solution:
    def uniquePathsIII(self, grid):
        target = (None, None)
        start = (None, None)
        todo = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    target = (i, j)
                elif grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] != -1:  # no blockage
                    todo += 1

        def neighbors(row, col):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for each_dir in directions:
                nr = row + each_dir[0]
                nc = col + each_dir[1]
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] % 2 == 0:  # only when the value != 2
                    yield (nr, nc)

        def dfs(row, col, left_over):
            left_over -= 1
            if left_over < 0:
                return
            if row == target[0] and col == target[1]:
                if left_over == 0:
                    self.ans += 1
                return
            grid[row][col] = -1  # mark visited
            for each_neighbor in neighbors(row, col):
                dfs(each_neighbor[0], each_neighbor[1], left_over)
            grid[row][col] = 0  # back_track to 0

        self.ans = 0
        dfs(start[0], start[1], todo)
        return self.ans


s = Solution()

grid1 = [[1, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 2, -1]]
grid2 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
grid3 = [[0, 1], [2, 0]]

print(s.uniquePathsIII(grid1))
print(s.uniquePathsIII(grid2))
print(s.uniquePathsIII(grid3))
