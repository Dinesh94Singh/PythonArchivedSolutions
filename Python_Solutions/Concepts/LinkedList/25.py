"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):
    p1 = head
    while p1:
        print(p1.val)
        p1 = p1.next

def reverse_k_group(head, k):
    count, node = 0, head
    # check if there are k nodes, if not there, don't need to reve
    while node and count < k:
        node = node.next
        count += 1
    if count < k:
        return head
    new_head, prev = reverse_k(head, k) # head is our start
    head.next = reverse_k_group(new_head, k)
    return prev

def reverse_k(head, k):
    p1 = head
    prev = None
    while k > 0 and p1:
        temp = p1.next
        p1.next = prev
        prev = p1
        p1 = temp
        k -= 1
    return p1, prev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print_list(head)
head = reverse_k_group(head, 2)
print_list(head)
