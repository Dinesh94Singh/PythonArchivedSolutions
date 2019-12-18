"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = float("-inf")

    def helper(self, root):
        if root is None:
            return 0
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        total_sum = root.val + left + right
        print(total_sum)
        self.ans = max(self.ans, total_sum)
        return max(left, right) + root.val

    def max_path_sum(self, root):
        self.helper(root)
        return self.ans


# [-10,9,20,null,null,15,7]
root = Tree(-10)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

s = Solution()
print(s.max_path_sum(root))
