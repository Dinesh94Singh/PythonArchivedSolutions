"""
Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)



Example 1:



Input: [5,6,1]
Output: 6.00000
Explanation:
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        max_avg = float('-inf')
        def dfs(root):
            nonlocal max_avg
            if not root:
                return (0, 0)
            l, l_count = dfs(root.left)
            r, r_count = dfs(root.right)
            total = root.val + l + r
            count = l_count + r_count + 1
            max_avg = max(max_avg, total / count)
            return (total, count)
        dfs(root)
        return max_avg
