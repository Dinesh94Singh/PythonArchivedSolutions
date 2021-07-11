"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_cousins(root, x, y):
    q = deque([(None, root)])
    while q:
        n = len(q)
        parent = {}
        for _ in range(n):
            par, node = q.popleft()
            parent[node.val] = par
            if node.left:
                q.append((node, node.left))
            if node.right:
                q.append((node, node.right))
        if x in parent and y in parent:
            return parent[x] != parent[y]  # check if parent x is not equal to parent y
        elif x in parent or y in parent:
            return False  # they are in different levels
    return False


class Solution():
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([(root, None, 0)])

        temp = []
        while queue:
            n = len(queue)
            for idx in range(n):
                node, parent, level = queue.popleft()

                if node.val == x or node.val == y:
                    if len(temp) == 1:
                        # compare the level and parent
                        other = temp[0]
                        if level == other[0] and parent != other[1]:
                            return True
                        return False
                    else:
                        temp.append((level, parent))

                if node.left:
                    queue.append((node.left, node, level + 1))
                if node.right:
                    queue.append((node.right, node, level + 1))
        return False


# [1,2,3,null,4,null,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

s = Solution()
print(s.isCousins(root, 5, 4))