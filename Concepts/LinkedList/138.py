"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the
list or null.

Return a deep copy of the list.


Example 1:

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
def print_list(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
    print('\n')

def copyRandomList(head: 'Node') -> 'Node':
    node = head
    while node:
        new_node = Node(node.val, node.next, None)
        node.next = new_node
        node = node.next.next
    print_list(head)

    node = head
    while node and node.next:
        node.next.random = node.random.next if node.random else None
        node = node.next.next

    print_list(head)

    old_head = head
    new_head = head.next
    node = old_head
    new_node = new_head
    while node:
        node.next = node.next.next
        new_head.next = new_head.next.next if new_head.next else None
        node = node.next
        new_node = new_node.next
    print_list(old_head)

head = Node(1, None, None)
head.next = Node(2, None, None)
head.random = head.next
head.next.random = head.next

print_list(head)
copyRandomList(head)
