import collections
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(row, col):
            visited = [[False] * n for _ in range(m)]
            dq = collections.deque([(row, col, 0)])
            count = 1
            visited[row][col] = True

            while dq:
                r, c, dist = dq.popleft()

                for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= x < m and 0 <= y < n and visited[x][y] == False:
                        visited[x][y] = True

                        if grid[x][y] == 0:
                            dq.append((x, y, dist + 1))
                            hit[x][y] += 1
                            dist_grid[x][y] += (dist + 1)
                        elif grid[x][y] == 1:
                            count += 1

            return count == total_buildings

        m = len(grid)
        n = len(grid[0])

        total_buildings = sum(val for line in grid for val in line if val == 1)

        dist_grid = [[0] * n for _ in range(m)]
        hit = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not bfs(i, j):  # if its not possible for one, its not possible for others as well.
                        return -1
        return min([dist_grid[i][j] for i in range(m) for j in range(n) if
                    not grid[i][j] and hit[i][j] == total_buildings] or [-1])