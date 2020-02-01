'''
73. Set Matrix Zeroes


Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

'''

def setZeroes(matrix):
    row = set()
    column = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                column.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row or j in column:
                matrix[i][j] = 0
    print(matrix)

def setZeroes_with_O1_space(matrix):
    ''' Use an additional variable for either row/column. Use variable is_col for first column and matrix[0][0] for first row '''
    is_col = False
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        ''' if a zero is found in first column, mark it '''
        ''' if the state is not maintained, you will loose the track of real 0 vs modified 0 '''
        if matrix[i][0] == 0:
            is_col = True

        for j in range(1, cols):
            ''' if the element is zero, set the first element of corresponding row and column '''
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[j][0] = 0
    ''' Iterate again and set the first element of corresponding row and column to 0 '''
    for i in range(1, rows):
        for j in range(1, cols):
            if not matrix[i][0] == 0 or not matrix[0][j] == 0:
                matrix[i][j] = 0
    ''' Check if the first row needs to be set 0 '''
    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0
    ''' Check if the first col needs to be set 0 '''
    if is_col:
        for i in range(rows):
            matrix[i][0] = 0
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

setZeroes(matrix)