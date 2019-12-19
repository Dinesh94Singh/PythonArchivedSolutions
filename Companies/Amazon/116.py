from collections import deque

class Node:
    def __init__(self, val, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque([root])

        while q:
            n = len(q)
            elements_at_level = []

            for i in range(n):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    elements_at_level.append(node.left)

                if node.right:
                    q.append(node.right)
                    elements_at_level.append(node.right)

            # we should have all the elements at this level

            for idx in range(len(elements_at_level) - 1):
                elements_at_level[idx].next = elements_at_level[idx - 1]

            if elements_at_level:
                elements_at_level[-1].next = None

        root.next = None
        return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

s = Solution()
s.connect(root)