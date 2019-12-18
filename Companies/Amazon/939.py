"""
939. Minimum area of a rectangle
"""

"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points,
with sides parallel to the x and y axes.

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

"""
Idea -> group based on x & y's -> 1: 1, 3
                                  3: 1, 3
                                  2: 2
"""

import collections

def min_area_rect(points):

    grouper_x = collections.defaultdict(list)

    for each_point in points:
        grouper_x[each_point[0]].append(each_point[1]) # groups x cords

    x_cords = grouper_x.keys()

    '''
        To form a rectangle -> either of x or y should be same
        
        min_area comes for either min l and min breadth
        
        for x in sorted(columns):
            # column would be 1 -> [1, 3], 3 -> [1, 3]
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in last_x:
                        self.ans = min(self.ans, (x-last_x[(y1, y2)]) * (y2 - y1))
                    last_x[(y1, y2)] = x
        return self.ans if self.ans < float('inf') else 0 
    '''

    last_x = {}

    ans = float('inf')

    for each_x_cord in sorted(x_cords):
        y_cords = x_cords[each_x_cord]
        for i, y_cord in sorted(y_cords):
            for j in range(i):
                # get the other cord apart from the current one
                other_y_cord = y_cords[j]

                if (y_cord, other_y_cord) in last_x:
                    ans = min(ans, (each_x_cord - last_x[(y_cord, other_y_cord)] * (y_cord - other_y_cord)))
                last_x[(y_cord, other_y_cord)] = each_x_cord

    return ans if ans != float('inf') else -1



