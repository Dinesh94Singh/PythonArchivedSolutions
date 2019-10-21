"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def start(self, head: ListNode) -> bool:
        slow, fast = head, head
        has_cycle = False
        while slow and fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                # There is cycle - find the length
                x = slow.next
                length = 0
                while x != slow:
                    x = x.next
                    length += 1
                print(length)
                break
        if has_cycle:
            p1 = head
            p2 = head
            while length >= 0:
                p2 = p2.next
                length -= 1
            while p1 and p2 and p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1



node = ListNode(3)
node.next = ListNode(2)
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)
node.next.next.next.next = node.next

s = Solution()
s.hasCycle(node)
s.start(node)

# Follow up - Find the starting point of the cycle
