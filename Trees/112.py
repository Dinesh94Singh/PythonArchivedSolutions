"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such
that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        def dfs(root, total):
            if not root and total == 0:
                return True
            elif not root:
                return False
            else:
                return dfs(root.left, total - root.val) or dfs(root.right, total - root.val)
        return dfs(root, total)

s = Solution()

# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
# root.left.left = TreeNode(11)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.right.right = TreeNode(1)

anotherRoot = TreeNode(1)
anotherRoot.left = TreeNode(2)

s.hasPathSum(anotherRoot, 1)
