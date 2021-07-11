'''
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

def spiralOrder(matrix):
    def spiral_coords(r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1

    if not matrix: return []
    ans = []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_coords(r1, c1, r2, c2):
            ans.append(matrix[r][c])
        r1 += 1; r2 -= 1
        c1 += 1; c2 -= 1
    return ans

'''
     c1        c2    
  r1 [1, 2, 3, 4],
     [5, 6, 7, 8],
  r2 [9,10,11,12]
'''

class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        r1, r2, c1, c2 = 0, rows - 1, 0, cols - 1

        res = []

        while r1 <= r2 and c1 <= c2:
            for i in range(c1, c2 + 1):
                res.append(matrix[r1][i])
            r1 += 1

            for i in range(r1, r2 + 1):
                res.append(matrix[i][c2])
            c2 -= 1

            if r1 <= r2:
                for i in range(c2, c1 - 1, -1):
                    res.append(matrix[r2][i])
                r2 -= 1

            if c1 <= c2:
                for i in range(r2, r1 - 1, -1):
                    res.append(matrix[i][c1])
                c1 += 1

        return res