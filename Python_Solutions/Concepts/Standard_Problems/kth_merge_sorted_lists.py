"""
Problem Statement
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
"""

## if we know the total count then total_count - kth pos is the res

import heapq


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value


def kth_merge_sorted_lists(lists, k):
    heap = []
    for each in lists:
        heapq.heappush(heap, each)

    c = 0
    while heap:
        node = heapq.heappop(heap)
        c += 1
        if c == k:
            return node
        if node.next is not None:
            heapq.heappush(heap, node.next)
    return None


l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

res = kth_merge_sorted_lists([l1, l2, l3], 1)
if res is not None:
    print(res.value)
else:
    print(None)
