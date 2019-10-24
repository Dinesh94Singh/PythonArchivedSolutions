"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        res = []

        def dfs(root, total, path):
            if not root:
                return None
            if not root.left and not root.right and total - root.val == 0:
                path.append(root.val)
                res.append(path)
            else:
                path.append(root.val)
                dfs(root.left, total - root.val, list(path))
                dfs(root.right, total - root.val, list(path))

        dfs(root, sum, [])
        return res


s = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.left = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.left = TreeNode(1)

print(s.pathSum(root, 22))
