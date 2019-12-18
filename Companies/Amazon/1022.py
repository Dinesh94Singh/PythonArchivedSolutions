"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.



Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root, num):
            nonlocal ans
            if not root:
                return
            n = num * 10 + root.val
            if root.left is None and root.right is None:
                # we have reached the bottom
                # n is a binary number
                print(n)
                dec = 0
                i = 0
                while n != 0:
                    dec += n % 10 * (2 ** i)
                    i += 1
                    n = n // 10
                ans += dec
            dfs(root.left, n)
            dfs(root.right, n)

        ans = 0
        dfs(root, 0)
        return ans
    
s = Solution()

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

root = TreeNode(1)
root.left = TreeNode(1)

s.sumRootToLeaf(root)