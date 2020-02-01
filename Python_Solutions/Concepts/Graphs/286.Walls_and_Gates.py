from collections import deque
from typing import List


def wallsAndGates(grid: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """

    def get_sources():
        sources = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    sources.append((i, j, 0))

        print(sources)

        return sources

    def get_directions(r, c):
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= r + x < len(grid) and 0 <= c + y < len(grid[0]):
                yield r + x, c + y

    dq = deque(get_sources())

    while dq:
        r, c, cost = dq.popleft()

        if cost < grid[r][c]:
            grid[r][c] = cost

        for x, y in get_directions(r, c):
            if grid[x][y] != -1 and grid[x][y] != 0 and grid[x][y] >= cost + 1:
                dq.append((x, y, cost + 1))

    for each_row in grid:
        print(each_row)


grid = [[2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]]

wallsAndGates(grid)
