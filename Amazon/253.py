import heapq


def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x[1])  # sort based on the start times
    heap = []
    heapq.heappush(heap, intervals[0][1])  # heap should have the end times.

    for idx in range(1, len(intervals)):
        interval = intervals[idx]
        print(interval, heap[-1])
        if interval[0] < heap[-1]:
            # the meeting starts before the first meeting which ends, assign a new room
            heapq.heappush(heap, interval[1])
        else:
            heapq.heappop(heap)  # re-assign the same meeting room
            print(heap)
            heapq.heappush(heap, interval[1])

    return len(heap)


# print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(minMeetingRooms([[2, 11], [6, 16], [11, 16]]))  # expected - 2 ??
