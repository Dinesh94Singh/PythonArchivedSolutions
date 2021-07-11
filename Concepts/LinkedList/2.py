"""

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
from node import ListNode


def add_two_numbers(l1, l2):
    carry = 0
    dummy = head = ListNode(0)
    while l1 or l2:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        val = l1_val + l2_val + carry
        carry = val // 10
        remainder = val % 10
        x = ListNode(remainder)
        dummy.next = x
        dummy = x
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry > 0:
        dummy.next = ListNode(carry)
    return head.next


