"""
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
"""
from collections import deque

def treasure_island(grid):
    def get_source():
        nonlocal m, n
        sources = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sources.append((i, j, 0))
        return sources

    def check_cond(x, y):
        nonlocal m, n, grid
        if x >= 0 and y >= 0 and x < m and y < n and grid[x][y] != 'D':
            return True
        return False

    m = len(grid)
    n = len(grid[1])
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque(get_source())
    visited = set()
    min_dist = float('inf')
    while queue:
        length = len(queue)
        for i in range(length):
            # print(visited)
            x, y, dist = queue.popleft()
            if (x, y) not in visited:
                visited.add((x, y))
            else:
                continue
            if grid[x][y] == 'X':
                min_dist = min(min_dist, dist)
                continue
            for each_dir in dir:
                if check_cond(x+each_dir[0], y + each_dir[1]):
                    queue.append((x + each_dir[0], y + each_dir[1], dist + 1))
    return min_dist if min_dist != float('inf') else -1


grid = [['S', '0', 'O', 'S', 'S'],
        ['D', '0', 'D', '0', 'D'],
        ['O', '0', '0', 'O', 'X'],
        ['0', 'D', 'D', 'O', '0'],
        ['0', 'D', '0', 'D', 'O']]

treasure_island(grid)
