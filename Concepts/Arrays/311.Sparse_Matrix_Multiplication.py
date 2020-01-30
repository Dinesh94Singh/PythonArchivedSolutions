"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

from typing import List

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        For matrix mux, col1 and row2 should be equal and the result would be of size row1*col2
        """
        row1 = len(A)
        col1 = len(A[0]) if row1 > 0 else 0
        row2 = len(B)
        col2 = len(B[0]) if row2 > 0 else 0

        if col1 != row2:
            raise ArithmeticError()

        res = [[0 for _ in range(col2)] for _ in range(row1)]

        for i in range(row1):
            for j in range(col2):
                for k in range(row2):
                    res[i][j] += A[i][k] * B[k][j]

        return res

    def multiply_optimized(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
            since sparse matrix, we can add a check 
        """
        row1 = len(A)
        col1 = len(A[0]) if row1 > 0 else 0
        row2 = len(B)
        col2 = len(B[0]) if row2 > 0 else 0

        if col1 != row2:
            raise ArithmeticError()

        res = [[0 for _ in range(col2)] for _ in range(row1)]

        for i in range(row1):
            for j in range(col2):
                if A[i][k] != 0:
                    # the product would any w
                    for k in range(row2):
                        res[i][j] += A[i][k] * B[k][j]

        return res

    def multiply_math_theroy(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        A sparse matrix can be represented as a sequence of rows, each of which is a sequence of (column-number, value) pairs of the nonzero values in the row.
        """
        pass

    def multiply_table_appraoch(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
            The idea is to create, hashmap for indexes on B whose values are not 0.

            One might think that, two hashmaps can be created both on A and B, and only loop on these hashmaps, and fill those values and leave the rest of them as zero. But, One HashMap is also a good solution.
        """
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        C = [[0 for _ in range(l)] for _ in range(m)]
        tableB = {}
        
        # O(n^2)
        for k, row in enumerate(B):
            tableB[k] = {} # populate tableB with [i][j] with ele val if B[i][j] != 0
            for j, eleB in enumerate(row):
                if eleB: tableB[k][j] = eleB
        # still, O(n^3) => But instead of looping through all the columns, which could have 0, we only loop through the ones, which are non-zero
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in tableB[k].iteritems():
                        C[i][j] += eleA * eleB
        return C
    
    def multiply_2_table_appraoch(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if A is None or B is None: return None
        m, n, p, q = len(A), len(A[0]), len(B), len(B[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        C = [[0 for _ in range(q)] for _ in range(m)]
        table_A = {}
        table_B = {}

        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    table_A[(i, j)] = A[i][j]

        for i in range(p):
            for j in range(q):
                if B[i][j] != 0:
                    table_B[(i, j)] = B[i][j]
        
        for pair, val in table_A.items():
            for other_pair, other_val in table_B.items():
                x1, y1 = pair
                x2, y2 = other_pair
                if y1 == x2:
                    C[x1][y2] += val * other_val

        return C

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

s = Solution()
# print(s.multiply(A, B))
print(s.multiply_2_table_appraoch(A, B))

