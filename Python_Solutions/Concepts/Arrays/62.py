"""

62. Unique paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

"""


def uniquePath(m, n):
    # @return an integer
    grid = [[1 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
    print(grid)
    return grid[-1][-1]  # last element in the grid


from collections import deque


def uniquePathRetry(m, n):
    directions = [(0, 1), (1, 0)]

    grid = [[0 for _ in range(n)] for _ in range(m)]

    count = 0
    q = deque([(0, 0)])

    while q:
        print(q)
        row, col = q.popleft()

        if row == m - 1 and col == n - 1:
            count += 1
            continue

        for r, c in directions:
            x = row + r
            y = col + c

            if 0 <= x < m and 0 <= y < n and grid[x][y] != 1:
                q.append((x, y))

    return count



def uniquePathRetry_Dp(m, n):

    grid = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[-1][-1]

# uniquePath(3, 2)

print(uniquePathRetry(7, 3))
print(uniquePathRetry_Dp(7, 3))
