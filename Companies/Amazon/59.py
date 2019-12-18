"""
59. Spiral Matrix - II
"""

"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row_start = 0
        row_end = n - 1
        col_start = 0
        col_end = n - 1

        res = [[0 for _ in range(3)] for _ in range(3)]

        counter = 1

        while row_start <= row_end and col_start <= col_end:
            # iterate the first row and add to res
            for c in range(col_start, col_end + 1):
                res[row_start][c] = counter
                counter += 1

            row_start += 1

            # iterate the last col and add to res
            for r in range(row_start, row_end + 1):
                res[r][col_end] = counter
                counter += 1

            col_end -= 1

            # iterate the bottom and add to res
            for c in range(col_end, col_start - 1, -1):
                res[row_end][c] = counter
                counter += 1
            row_end -= 1

            for r in range(row_end, row_start - 1, -1):
                res[r][col_start] = counter
                counter += 1
            col_start += 1

        return res

s = Solution()
grid = s.generateMatrix(3)

for each in grid:
    print(each)