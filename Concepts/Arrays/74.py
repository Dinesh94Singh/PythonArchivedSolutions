"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
"""


class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        row = rows - 1
        col = 0

        while row >= 0 and col < cols:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1

        return False


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

s = Solution()
print(s.searchMatrix(matrix, 13))
