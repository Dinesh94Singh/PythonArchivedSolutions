"""
542. 01 Matrix
"""

"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

from typing import List

class Solution:
    def updateMatrix(self, A):
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for cr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        q = collections.deque([((r, c), 0)
                               for r in xrange(R)
                               for c in xrange(C)
                               if A[r][c] == 0])
        seen = {x for x, _ in q}
        ans = [[0] * C for _ in A]
        while q:
            (r, c), depth = q.popleft()
            ans[r][c] = depth
            for nei in neighbors(r, c):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth + 1))

        return ans

# grid = [[0,0,0],
#         [0,1,0],
#         [0,0,0]]

s = Solution()
# res = s.updateMatrix(grid)
# for each in res:
#     print(each)
#
# print('\n\n')
#
# grid2 = [[0,0,0],
#          [0,1,0],
#          [1,1,1]]
# res = s.updateMatrix(grid2)
# for each in res:
#     print(each)

grid3 = [[1,0,1,1,0,0,1,0,0,1],
         [0,1,1,0,1,0,1,0,1,1],
         [0,0,1,0,1,0,0,1,0,0],
         [1,0,1,0,1,1,1,1,1,1],
         [0,1,0,1,1,0,0,0,0,1],
         [0,0,1,0,1,1,1,0,1,0],
         [0,1,0,1,0,1,0,0,1,1],
         [1,0,0,0,1,1,1,1,0,1],
         [1,1,1,1,1,1,1,0,1,0],
         [1,1,1,1,0,1,0,0,1,1]]

print('\n\n')
res = s.updateMatrix(grid3)
for each in res:
    print(each)

"""
expected-output:
[[1,0,1,1,0,0,1,0,0,1],
 [0,1,1,0,1,0,1,0,1,1],
 [0,0,1,0,1,0,0,1,0,0],
 [1,0,1,0,1,1,1,1,1,1],
 [0,1,0,1,1,0,0,0,0,1],
 [0,0,1,0,1,1,1,0,1,0],
 [0,1,0,1,0,1,0,0,1,1],
 [1,0,0,0,1,2,1,1,0,1],
 [2,1,1,1,1,2,1,0,1,0],
 [3,2,2,1,0,1,0,0,1,1]]
"""
