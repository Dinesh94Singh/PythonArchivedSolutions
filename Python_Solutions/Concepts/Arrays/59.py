'''
59. Spiral Matrix 2
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[    0     n
 0 [ 1, 2, 3 ],
   [ 8, 9, 4 ],
 n [ 7, 6, 5 ]
]
'''
def generateMatrix(n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A

generateMatrix(3)