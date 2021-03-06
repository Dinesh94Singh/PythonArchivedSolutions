"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_balanced(self, root):
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1

        if not root:
            return True
        diff = abs(depth(root.left) - depth(root.right))
        if diff > 1:
            return False
        return self.is_balanced(root.left) and self.is_balanced(root.right)

