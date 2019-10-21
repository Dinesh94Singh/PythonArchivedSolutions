"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""


class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_depth = 0

    def max_depth_recursive(self, root):
        def depth(root):
            if root is None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return max(left, right) + 1
        return depth(root)

    def max_depth_iterative(self, root):
        stack = [(0, root)]
        while stack:
            curr_depth, node = stack.pop()
            self.max_depth = max(self.max_depth, curr_depth)
            if node:
                stack.append((curr_depth + 1, node.left))
                stack.append((curr_depth + 1, node.right))
        return self.max_depth


root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

s = Solution()

s.max_depth_iterative(root)
s.max_depth_recursive(root)
