"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    res = []
    for idx in range(1, len(intervals)):
        interval = intervals[idx]
        if (end >= interval[0] and start <= interval[1]) or (interval[1] >= start and interval[0] <= end):
            start = min(start, interval[0])
            end = max(end, interval[1])
        else:
            res.append([start, end])
            start = interval[0]
            end = interval[1]
    res.append([start, end])
    return res

print(merge([[1,3],[2,6],[8,10],[15,18]]))

print(merge([[1,4],[4,5]]))

print(merge([[1, 4], [0, 3]]))

print(merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
