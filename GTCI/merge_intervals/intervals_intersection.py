"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted
on their start time

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""


def interval_intersection(intervals_1, intervals_2):
    i = 0
    j = 0
    results = []
    while i < len(intervals_1) and j < len(intervals_2):
        interval_a = intervals_1[i]
        interval_b = intervals_2[j]
        # check if there is a overlap
        if (interval_b[0] <= interval_a[0] <= interval_b[1]) or (interval_a[0] <= interval_b[0] <= interval_a[1]):
            results.append([max(interval_a[0], interval_b[0]), min(interval_a[1], interval_b[1])])
        if interval_a[1] < interval_b[1]:
            # if interval_a ends before interval_b move i
            i += 1
        else:
            j += 1
    return results


interval_intersection([[1, 3], [5, 7], [9, 12]], [[5, 10]])
interval_intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])
