"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are
overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as
the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def merge_trees_recursive(self, t1, t2):
        if not t1 and not t2:
            return None
        if not t1 and t2:
            return t2
        if not t2 and t1:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.merge_trees(t1.left, t2.left)
        t1.right = self.merge_trees(t1.right, t2.right)
        return t1

    def merge_trees_iterative(self, t1, t2):
        stack = [(t1, t2)]
        while stack:
            v1, v2 = stack.pop()
            if not v1 or not v2:
                continue
            v1.val += v2.val
            if v1.left == None:
                v1.left = v2.left
            else:
                stack.push((v1.left, v2.left))
            if v1.right == None:
                v1.right = v1.right
            else:
                stack.push((v1.right, v2.right))
        return t1

t1 = Tree(1)
t1.left = Tree(3)
t1.right = Tree(2)
t1.left.left = Tree(5)

t2 = Tree(2)
t2.left = Tree(1)
t2.right = Tree(3)
t2.left.right = Tree(4)
t2.right.right = Tree(7)

s = Solution()
s.merge_trees(t1, t2)
