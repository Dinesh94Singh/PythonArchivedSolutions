"""
48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


# def rotate(self, matrix: List[List[int]]) -> None:

def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
    print('Rotated is', matrix)


rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def rotate_2(grid):
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(grid)):
        for j in range(i, len(grid[0])):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    for i in range(len(grid)):
        grid[i].reverse()
    print(grid)
    return grid

rotate_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])