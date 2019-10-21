"""
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms
required to hold all the meetings.

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
occur in any of the two rooms later.

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to
hold all the meetings.

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

Here is a visual representation of Example 4:
"""

import heapq


def min_meeting_rooms(meetings):
    i = 1
    meetings.sort(key=lambda x: x[0])
    results = []
    heapq.heappush(results, meetings[0][1])
    while i < len(meetings):
        curr_meeting = meetings[i]
        top = results[0]
        if curr_meeting[0] >= top:
            # check if there is a overlap. Curr meeting starts after a meeting is done
            heapq.heappop(results)
        heapq.heappush(results, curr_meeting[1])
        i += 1
    return len(results)


min_meeting_rooms([[6, 7], [2, 4], [8, 12]])
min_meeting_rooms([[4, 5], [2, 3], [2, 4], [3, 5]])
min_meeting_rooms([[1, 4], [2, 3], [3, 6]])
