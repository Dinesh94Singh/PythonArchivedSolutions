"""
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
"""


def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    i = 0
    result = True
    while i < len(intervals) - 1:
        if intervals[i][1] < intervals[i + 1][0]:
            # this meeting has to end before the next meeting
            i += 1
        else:
            result = False
            break
    return result


can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])
can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])
can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])
