"""
417. Pacific Atlantic Water flow
"""

"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right
and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pacific_queue = deque([])
        atlantic_queue = deque([])

        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        """
            - add all the left and top to pacific
            - all right and bottom to atlantic
        """
        

        """ Adding top and left """
        for i in range(cols):
            pacific_queue.append([0, i])
            atlantic_queue.append([rows - 1, i])
        for i in range(rows):
            pacific_queue.append([i, 0])
            atlantic_queue.append([i, cols - 1])


        """ Perform a BFS from the queues """
        def perform_bfs(queue):
            def check_cond(row, col):
                if 0 <= row < rows and 0 <= col < cols and not visited[row][col]:
                    return True
                return False

            visited = [[False for _ in range(cols)] for _ in range(rows)]
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            while queue:
                r, c = queue.popleft()
                visited[r][c] = True
                for each_dir in directions:
                    row = r + each_dir[0]
                    col = c + each_dir[1]

                    """ Only add elements bigger than the current element """
                    if check_cond(row, col) and matrix[r][c] <= matrix[row][col]:
                        queue.append([row, col])

            return visited


        pacific = perform_bfs(pacific_queue)
        atlantic = perform_bfs(atlantic_queue)

        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res


matrix = [[1,2,2,3,5],
          [3,2,3,4,4],
          [2,4,5,3,1],
          [6,7,1,4,5],
          [5,1,1,2,4]]

s = Solution()
print(s.pacificAtlantic(matrix))