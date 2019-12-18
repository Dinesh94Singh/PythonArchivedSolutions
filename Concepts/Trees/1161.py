"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.



Example 1:



Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return -1
        queue = deque([(root, 1)])
        maximum = (root.val, 1)
        while queue:
            n = len(queue)
            total = 0
            for _ in range(n):
                node, level = queue.popleft()
                if node.left is not None:
                    total += node.left.val
                    queue.append((node.left, level + 1))
                if node.right is not None:
                    total += node.right.val
                    queue.append((node.right, level + 1))
            if total > maximum[0]:
                maximum = (total, level + 1)
        return maximum[1]
