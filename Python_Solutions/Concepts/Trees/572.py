"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check_equality(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and check_equality(s.left, t.left) and check_equality(s.right, t.right)

        def dfs(root):
            if not root:
                return False
            return check_equality(root, t) or dfs(root.left) or dfs(root.right)

        return dfs(s)

s = Solution()
# root = TreeNode(3)
# root.left = TreeNode(4)
# root.right = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
#
# print(s.isSubtree(root, TreeNode(7)))
root = TreeNode(1)
root.left = TreeNode(1)
root.right = None

root2 = TreeNode(1)
s.isSubtree(root, root2)
