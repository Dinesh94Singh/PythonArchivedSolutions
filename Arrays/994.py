"""
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

from collections import deque

def orangesRotting(grid):
    def getRottenIndices():
        nonlocal grid, d
        rotten_indices = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_indices.append((i, j, d)) # 0 for the time taken
        return rotten_indices
    def check_cond(i, j):
        nonlocal grid
        print(i, j)
        if i >= 0 and i < len(grid) and j >=0 and j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 2
            return True
        return False
    d = 0
    queue = deque(getRottenIndices())
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        print(queue)
        x, y, d = queue.popleft()
        for each_dir in directions:
            if check_cond(x+each_dir[0], y+each_dir[1]):
                queue.append((x+each_dir[0], y+each_dir[1], d + 1))
    print(grid)
    if any(1 in row for row in grid):
        return -1
    return d

# print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
# print(orangesRotting([[0,2]]))
# print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(orangesRotting([[1],[2]]))
