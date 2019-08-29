'''

695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,X,0,X,0,0],
 [0,1,0,0,1,1,0,0,X,X,X,0,0],
 [0,0,0,0,0,0,0,0,0,0,X,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

'''
# Exceeds
def maxAreaOfIsland(grid):
    seen = set()
    ans = 0
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            if column and (row_index, column_index) not in seen:
                shape = 0
                stack = [(row_index, column_index)]
                seen.add((row_index, column_index))
                while stack:
                    r, c = stack.pop()
                    shape += 1
                    if r == 0 and c == 0:
                        print(r, c)
                    for sorrounding_row, sorrounding_column in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= sorrounding_row < len(grid) and 0 <= sorrounding_column < len(grid[0]):
                            stack.append((sorrounding_row, sorrounding_column))
                            seen.add((sorrounding_column, sorrounding_row))
                ans = max(ans, shape)
    return ans

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

maxAreaOfIsland(grid)