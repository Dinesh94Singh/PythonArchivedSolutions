"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive
intervals.

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""


def merge_interval(intervals):
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        print(interval, start, end)
        if interval[0] <= end:
            # there is a overlap
            start = min(start, interval[0])
            end = max(end, interval[1])
        else:
            merged_intervals.append([start, end])
            start = interval[0]
            end = interval[1]
    merged_intervals.append([start, end])
    print(merged_intervals)


merge_interval([[1, 4], [2, 6], [3, 5]])
merge_interval([[6, 7], [2, 4], [5, 9]])
merge_interval([[1, 4], [2, 5], [7, 9]])
