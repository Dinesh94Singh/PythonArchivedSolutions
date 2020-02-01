"""
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
"""

import heapq


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value


def merge_k_sorted_lists(lists):
    heap = []

    for each in lists:
        heapq.heappush(heap, each)

    head = tail = None

    while heap:
        node = heapq.heappop(heap)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = tail.next
        if node.next is not None:
            heapq.heappush(heap, node.next)
    return head


l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)
result = merge_k_sorted_lists([l1, l2, l3])

while result:
    print(str(result.value) + " ", end='')
    result = result.next
