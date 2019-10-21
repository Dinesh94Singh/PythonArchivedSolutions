"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:

The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root):
        res = []
        def level_order_bottom_dfs(root):
            def dfs(root, depth):
                if root is None:
                    return
                if len(res) > depth:
                    res[depth].append(root.val)
                else:
                    res.append([root.val])
                dfs(root.left, depth + 1)
                dfs(root.right, depth + 1)
            dfs(root, 0)
            return res[::-1]
        level_order_bottom_dfs(root)
        result = []
        for each in res:
            result.append(sum(each)/len(each))
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
s.averageOfLevels(root)
