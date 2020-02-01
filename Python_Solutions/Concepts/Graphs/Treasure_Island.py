"""
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""
from collections import deque

def treasure_island(grid):
    i, j = 0, 0
    m = len(grid) # 4
    n = len(grid[0]) # 4
    queue = deque([(i, j, 0), ])
    visited = set()
    min_dist = float('inf')
    count = 0
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) not in visited:
            visited.add((x, y))
        else:
            continue
        # print(x, y)
        if grid[x][y] == 'X' and x >= 0 and y >= 0 and x < m and y < n:
            print(x, y)
            count += 1
            # if we reached the treasure location, find the least path to reach here
            min_dist = min(min_dist, dist)
            continue
        if x < m - 1 and x >= 0 and grid[x+1][y] != 'D':
            queue.append((x+1, y, dist + 1))
        if x < m - 1 and x >=0 and grid[x-1][y] != 'D':
            queue.append((x-1, y, dist + 1))
        if y < n - 1and y >= 0 and grid[x][y+1] != 'D':
            queue.append((x, y+1, dist + 1))
        if y < n - 1 and y >= 0 and grid[x][y+1] != 'D':
            queue.append((x, y-1, dist + 1))
    print('count', count)
    return min_dist if min_dist != float('inf') else -1
grid = [
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'X']
]

print(treasure_island(grid))

grid2 = [
 ['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'D', 'D', 'X']
]

print(treasure_island(grid2))
