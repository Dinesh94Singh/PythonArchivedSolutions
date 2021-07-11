from typing import List
import bisect
import collections


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    idx = bisect.bisect_right(arr, x)
    left, right = idx - 1, idx
    queue = collections.deque()
    while k > 0:
        left_val = x - arr[left] if 0 <= left < len(arr) else float('inf')
        right_val = arr[right] - x if 0 <= right < len(arr) else float('inf')
        if left_val <= right_val:
            queue.appendleft(arr[left])
            left -= 1
        else:
            queue.append(arr[right])
            right += 1
        k -= 1
    res = list(queue)
    return res


print(findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(findClosestElements([1, 2, 200, 201, 202, 203], 4, 199))
print(findClosestElements([1, 2, 3, 4, 5], 4, -1))
print(findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))  # expected 3, 3, 4
