"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameter(self, root):
        self.ans = 1
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1
        depth(root)
        return self.ans - 1

class My_Solution:
    def diameter(self, root):
        def dfs(root):
            if not root:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)

            self.dia = max(self.dia, L + R + 1)
            return max(L, R) + 1

        self.dia = float('-inf')
        dfs(root)

        return self.dia
