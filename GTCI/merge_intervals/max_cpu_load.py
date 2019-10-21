"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:

Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the
jobs are running at the same time i.e., during the time interval (2,4).
Example 2:

Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.
Example 3:
"""


def max_cpu_load(jobs):
    jobs.sort(key=lambda x: x[0])
    max_load = jobs[0][2]
    start = jobs[0][0]
    end = jobs[0][1]
    load = jobs[0][2]
    i = 1
    while i < len(jobs):
        job = jobs[i]
        if job[0] < end:
            # they overlap - a overlap b and b overlap a - check both conditions ?
            print('max load at', [max(start, job[0]), min(end, job[1])])
            max_load = max(max_load, load + job[2])
            start = max(start, job[0])
            end = min(end, job[1])
            load = load + job[2]
        else:
            # they do not overlap
            max_load = max(max_load, job[2])
            start = job[0]
            end = job[1]
            load = job[2]
        i += 1
    return max_load


max_cpu_load([[1, 4, 3], [2, 5, 4], [7, 9, 6]])
max_cpu_load([[6, 7, 10], [2, 4, 11], [8, 12, 15]])
