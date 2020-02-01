"""
538. Greater Binary Tree from BST
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.maxSum = root.val + self.maxSum
            root.val = self.maxSum
            dfs(root.left)

        self.maxSum = 0

        dfs(root)

        return root


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

s = Solution()
s.convertBST(root)