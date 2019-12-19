def num_of_islands(grid):
    def dfs(row, col, grid):
        if row >=0 and len(grid) > row and col >= 0 and len(grid[1]) > col and grid[row][col] == 1:
            grid[row, col] = 0
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        else:
            return

from collections import deque

def num_of_islands_bfs(grid):
    def check_cond(row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[1]) and grid[row][col] == 1:
            return True
        return False
    if not grid or len(grid) == 0:
        return 0
    count = 0
    for i in len(grid):
        for j in len(grid[0]):
            if grid[i][j] == 1:
                q = deque([(i, j)])
                count += 1
                while q:
                    row, col = q.popleft()
                    grid[row][col] = 0
                    if check_cond(row + 1, col):
                        q.append((row + 1, col))
                    if check_cond(row - 1, col):
                        q.append((row - 1, col))
                    if check_cond(row, col + 1):
                        q.append((row, col + 1))
                    if check_cond(row, col - 1):
                        q.append((row, col - 1))
    return count
