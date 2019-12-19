"""
448. LinkedList Sum
"""

"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def find_length(l):
            c = 0
            while l:
                c += 1
                l = l.next

            return c

        def helper(l1_node, l2_node):
            carry = 0
            next_node = None
            if l1_node.next and l2_node.next:
                next_node, carry = helper(l1_node.next, l2_node.next)

            total = carry + l1_node.val + l2_node.val
            if total >= 10:
                carry = 1
                new_node = ListNode(total % 10)
            else:
                carry = 0
                new_node = ListNode(total)

            new_node.next = next_node

            return (new_node, carry)

        def helper2(l1_node, carry, steps):
            # TODO: Do similar to what helper1 did
            pass

        l1_length = find_length(l1)
        l2_length = find_length(l2)

        if l1_length > l2_length:
            pass
        else:
            l2, l1 = l1, l2

        # l1 is always larger now
        diff = abs(l1_length - l2_length)

        l_temp = l1
        tail = None
        for i in range(diff):
            tail = l_temp
            l_temp = l_temp.next

        node, carry = helper(l_temp, l2)

        return node


s = Solution()
list1 - ListNode(7)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

s.addTwoNumbers(list1, list2)
