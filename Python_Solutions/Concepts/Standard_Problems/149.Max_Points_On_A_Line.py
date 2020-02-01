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


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def is_same(p1, p2):
            return p1[0] == p2[0] and p1[1] == p2[1]

        def get_slope(p1, p2):
            if p1[1] == p2[1]: return 0
            if p1[0] == p2[0]: return float('inf')
            return decimal.Decimal((p2[1] - p1[1]) / (p2[0] - p1[0]))

        global_max = float('-inf')

        for idx, each_point in enumerate(points):
            local_max = 1
            same = 0
            slope_to_count_map = {}

            j = idx + 1
            while j < len(points):
                other_point = points[j]
                if is_same(each_point, other_point):
                    same += 1
                    continue
                slope = get_slope(each_point, other_point)
                print(slope)
                slope_to_count_map[slope] = slope_to_count_map.get(slope, 1) + 1
                local_max = max(local_max, slope_to_count_map[slope])
                j += 1

            global_max = max(global_max, local_max + same)

        return global_max if global_max != float('-inf') else 0
    

s = Solution()
# print(s.maxPoints([[1, 1], [2, 2], [3, 3]])) # 3
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])) # 4
print(s.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]])) # 2