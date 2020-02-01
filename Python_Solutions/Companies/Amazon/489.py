"""
498. Diagonal Traverse
"""

"""
Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

"""

from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        dd = collections.defaultdict(list)
        if not matrix: return result
        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i + j + 1].append(matrix[i][j])  # starting indices from 1, hence i+j+1.
        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        for k in sorted(dd.keys()):
            if k % 2 == 1: dd[k].reverse()
            result += dd[k]
        return result

