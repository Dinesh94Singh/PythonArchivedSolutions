"""
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).



Example 1:



Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation:
The path with the maximum score is highlighted in yellow.
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:



Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
"""

import heapq

class Solution:
    def maximumMinimumPath(self, matrix):
        de = ((1, 0), (0, 1), (-1, 0), (0, -1))
        rl, cl = len(matrix), len(matrix[0])
        q = [(-matrix[0][0], 0, 0)]
        memo = [[1 for _ in range(cl)] for _ in range(rl)] # visited array
        while q:
            t, x, y = heapq.heappop(q)
            if x == rl - 1 and y == cl - 1:
                return -t
            for d in de:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < rl and 0 <= ny < cl and memo[nx][ny]:
                    memo[nx][ny] = 0
                    heapq.heappush(q, (max(t, -matrix[nx][ny]), nx, ny))


class Solution_Doesnt_Work:
    def maximumMinimumPath(self, grid):
        def check_cond(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 'X':
                return True
            return False

        def dfs(r, c, path):
            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            t = []
            if check_cond(r, c):
                path.append(grid[r][c])
            grid[r][c] = 'X'

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                self.ans = min(path)

            for each_dir in dir:
                if check_cond(r + each_dir[0], c + each_dir[1]):
                    t.append((grid[r + each_dir[0]][c + each_dir[1]], r + each_dir[0], c + each_dir[1]))

            t.sort(key=lambda x: x[0], reverse=True)
            for each in t:
                # [2, 0, 5, 2, 0],
                # [2, 4, 4, 4, 3],
                # [1, 5, 0, 0, 0],
                # [5, 4, 4, 3, 1],
                # [1, 3, 1, 5, 3]
                dfs(each[1], each[2], path)

        if grid is None:
            return 0
        self.ans = float('inf')
        dfs(0, 0, [])

        return self.ans if self.ans != float('inf') else 0


s = Solution()
# print(s.maximumMinimumPath([[5, 4, 5], [1, 2, 6], [7, 4, 6]]))
# print(s.maximumMinimumPath([[2, 2, 1, 2, 2, 2],
#                             [1, 2, 2, 2, 1, 2]]
#                            ))
# print(s.maximumMinimumPath([[3, 4, 6, 3, 4],
#                             [0, 2, 1, 1, 7],
#                             [8, 8, 3, 2, 7],
#                             [3, 2, 4, 9, 8],
#                             [4, 1, 2, 0, 0],
#                             [4, 6, 5, 4, 3]]))
print(s.maximumMinimumPath([[2, 0, 5, 2, 0],
                            [2, 4, 4, 4, 3],
                            [1, 5, 0, 0, 0],
                            [5, 4, 4, 3, 1],
                            [1, 3, 1, 5, 3]]))
