"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

from typing import List
import collections
import decimal

import collections
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        p_len = len(points)
        if p_len <= 2:
            return p_len
        res = 0
        for i in range(p_len - 1):
            curr, overlap, lines = 0, 0, {}
            for j in range(i + 1, p_len):
                dx, dy = points[i][0] - points[j][0], points[i][1] - points[j][1]
                if dx == dy == 0:
                    overlap += 1
                    continue
                key = None if dx == 0 else 10.0 * dy / dx
                lines[key] = lines.get(key, 1) + 1
                curr = max(curr, lines[key])
            print(lines)
            res = max(res, curr + overlap)
        return res + 1
    

s = Solution()
# print(s.maxPoints([[1, 1], [2, 2], [3, 3]])) # 3
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])) # 4
# print(s.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]])) # 2