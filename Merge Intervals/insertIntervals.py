'''

Problem Statement
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
Try it yourself

'''


def insertIntervals(int_a, int_b):
    i, j = 0, 0
    start, end = 0, 1
    res = []
    while i < len(int_a) and j < len(int_b):
        left_interval = int_a[i]
        right_interval = int_b[j]
        if (right_interval[end] < left_interval[start]):
            # No match present, so move forward
            j += 1
        else:
            new_interval = []
            new_interval[start] = max(left_interval[start], right_interval[start])
            new_interval[end] = min(left_interval[end], right_interval[end])
            res.append(new_interval)
            i += 1



