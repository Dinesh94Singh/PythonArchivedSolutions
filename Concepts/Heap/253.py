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
import heapq


def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    rooms = []
    heapq.heappush(rooms, intervals[0][1])
    for i in range(1, len(intervals)):
        # rooms only hold the end times. If the end time is less than the current start time, we can allocate the room
        if intervals[i][0] >= rooms[0]:
            heapq.heappushpop(rooms, intervals[i][1])  # remove and add the curr interval
        else:
            heapq.heappush(rooms, intervals[i][1])  # allocate a new room
    return len(rooms)


min_meeting_rooms([[7, 10], [2, 4]])
min_meeting_rooms([[0, 30], [5, 10], [15, 20]])

# Time Complexity = O(NLogN)

