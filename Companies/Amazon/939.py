"""
Minimal Area of Rectangle
"""

"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed
from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""

import collections

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        last_x = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in last_x:
                        ans = min(ans, (x - last_x[y1,y2]) * (y2 - y1))
                        # trying to x2-x1 => where x2 is current x and x1 is prev x
                        # but to form a rectangle, they should be at the same vertices
                    last_x[y1, y2] = x
        return ans if ans < float('inf') else 0


s = Solution()
s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])