# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        prev = None
        while slow and fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # by the time slow reaches half the length, fast is at the end

        # reverse slow - end
        prev.next = None
        prev = None
        while slow:
            t = slow.next
            slow.next = prev
            prev = slow
            slow = t

        first_half = head
        other_half = prev

        while first_half and other_half:
            t = first_half.next
            first_half.next = other_half
            t2 = other_half.next
            other_half.next = t

            first_half = t
            other_half = t2

        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

s = Solution()
s.reorderList(head)