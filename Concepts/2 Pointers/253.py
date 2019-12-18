"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method
signature.

"""


def min_meeting_rooms_using_2_ptrs(intervals):
    start_array = sorted([i[0] for i in intervals])
    end_array = sorted([i[1] for i in intervals])

    used_rooms = 0
    start_ptr, end_ptr = 0, 0
    while start_ptr < len(intervals):
        if start_array[start_ptr] >= end_array[end_ptr]:
            # if the meeting starts after the previous meeting - we can use the same room
            used_rooms -= 1
            end_ptr += 1
        used_rooms += 1
        start_ptr += 1

    return used_rooms


min_meeting_rooms_using_2_ptrs([[7, 10], [2, 4]])
min_meeting_rooms_using_2_ptrs([[0, 30], [5, 10], [15, 20]])
