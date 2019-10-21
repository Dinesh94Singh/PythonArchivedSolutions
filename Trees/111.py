"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def min_depth(root):
    minimum = float('inf')
    def depth(root, d):
        nonlocal minimum
        if root is None:
            return d
        left = depth(root.left, d + 1)
        right = depth(root.right, d + 1)
        # print('left and right are ', left, right, 'root is ', root.val)
        minimum = min(minimum, min(left, right))
        return min(left, right)
    depth(root, 0)
    return minimum

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def min_depth(root):
    def depth(root):
        if root is None:
            return 0
        minimum = float('inf')
        left = depth(root.left)
        right = depth(root.right)
        minimum = min(minimum, min(left, right))
        return minimum + 1
    return depth(root)

def my_try(root):
    minimum = float('inf')
    def depth(root, d):
        nonlocal minimum
        if root is None:
            return 0
        left = depth(root.left, d + 1)
        right = depth(root.right, d + 1)
        # print('left and right are ', left, right, 'root is ', root.val)
        minimum = min(minimum, max(left, right) + 1)
        return max(left, right) + 1
    if root is None:
        return d
    depth(root, 0)
    return minimum + 1

min_depth(root)
my_try(root)
