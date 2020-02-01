"""

Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second
tree whose values sum up to a given integer target.



Example 1:



Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
    2            1
  /  \          / \
  1   4       0    3  => 2 + 3 =>
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:



Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false


Constraints:

Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        root1_cache = set()
        root2_cache = set()

        def dfs(root1, root2):
            if not root1 and not root2:
                return False
            if root1:
                x = target - root1.val
                if x in root2_cache:
                    return True
                root1_cache.add(root1.val)
            if root2:
                y = target - root2.val
                if y in root1_cache:
                    return True
                root2_cache.add(root2.val)

            root1_left = root1.left if root1 else None
            root1_right = root1.right if root1 else None

            root2_left = root2.left if root2 else None
            root2_right = root2.right if root2 else None

            return dfs(root1_left, root2_left) or dfs(root1_right, root2_right)

        return dfs(root1, root2)

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)

s = Solution()
print(s.twoSumBSTs(root1, root2, 5))

root3 = TreeNode(0)
root3.left = TreeNode(-10)
root3.right = TreeNode(10)

root4 = TreeNode(1)
root4.left = TreeNode(0)
root4.right = TreeNode(3)

print(s.twoSumBSTs(root3, root4, 18))