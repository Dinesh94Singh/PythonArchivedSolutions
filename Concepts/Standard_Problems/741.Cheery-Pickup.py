from collections import deque
from typing import List


class Solution(object):
    def cherryPickup(self, grid):
        def bestpath(grid):
            nonlocal N, dp

            for i in range(N - 1, -1, -1):
                for j in range(N - 1, -1, -1):
                    if grid[i][j] >= 0 and (i != N - 1 or j != N - 1):
                        dp[i][j] = max(dp[i + 1][j] if i + 1 < N else float('-inf'),
                                       dp[i][j + 1] if j + 1 < N else float('-inf'))
                        dp[i][j] += grid[i][j]

            if dp[0][0] < 0: return None
            ans = [(0, 0)]
            i = j = 0
            while i != N - 1 or j != N - 1:
                if j + 1 == N or i + 1 < N and dp[i + 1][j] >= dp[i][j + 1]:
                    i += 1
                else:
                    j += 1
                ans.append((i, j))
            return ans

        N = len(grid)
        dp = [[float('-inf')] * N for _ in range(N)]
        dp[-1][-1] = grid[-1][-1]

        ans = 0
        path = bestpath(grid)
        if path is None: return 0

        for i, j in path:
            ans += grid[i][j]
            grid[i][j] = 0

        for i, j in bestpath(grid):
            ans += grid[i][j]

        return ans


grid = [
    [1, 1, -1],
    [1, -1, 1],
    [-1, 1, 1]
]

grid2 = [
    [0, 1, -1],
    [1, 0, -1],
    [1, 1,  1]
]

s = Solution()
print(s.cherryPickup(grid2))
