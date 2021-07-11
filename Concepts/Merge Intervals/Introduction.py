'''

Merge Intervals

'''
def merge(intervals):
    if len(intervals) < 2:
        return intervals
    intervals.sort(key = lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    res = []
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= end:
            # overlapping
            end = max(end, interval[1])
        else:
            res.append([start, end])
            start = interval[0]
            end = interval[1]
    res.append([start, end])
    return res

print(merge([[1, 4], [2, 5], [7, 9]]))
