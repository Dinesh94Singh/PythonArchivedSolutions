# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def print_list(self, head):
        node = head
        while node:
            print(node.val, end=" ")
            node = node.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = l1
        j = l2
        head = dummy = ListNode(0)
        while i and j:
            if i.val < j.val:
                dummy.next = i
                i = i.next
            else:
                dummy.next = j
                j = j.next
            dummy = dummy.next
        if i:
            dummy.next = i
        elif j:
            dummy.next = j

        self.print_list(head.next)
        return head.next

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

s = Solution()
s.mergeTwoLists(head1, head2)
