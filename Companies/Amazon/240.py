"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        if matrix is None:
            return False
        row, col = len(matrix) - 1, 0
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if matrix[row][col] == target:
                print('found at ', row, col)
                return True
            elif matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
        return False

s = Solution()

matrix = [[1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]

matrix = [[-5]]

print(s.searchMatrix(matrix, 40))