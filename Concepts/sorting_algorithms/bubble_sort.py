class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def swap_nodes(node1, node2):
    if node1 and node2:
        temp = node1.next
        node1.next = node2
        node2.next = temp
        return node2


def find_length(node):
    d = node
    l = 0
    while d:
        l += 1
        d = d.next
    return l


def sort_list(head):
    count = find_length(head)

    for i in range(count):
        dummy = head
        total_swaps = 0

        for j in range(count - i - 1):
            p1 = dummy
            p2 = p1.next

            if p1.val > p2.val:
                dummy = swap_nodes(p1, p2)
                total_swaps = 1

            dummy = dummy.next

        if total_swaps == 0:
            break

    d = head
    while d:
        print(d.val, end='\t')
        d = d.next


head = Node(5)
head.next = Node(11)
head.next.next = Node(1)
head.next.next.next = Node(14)

sort_list(head)