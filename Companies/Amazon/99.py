"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def in_order_traversal(root):
            return in_order_traversal(root.left) + [root.val] + in_order_traversal(root.right) if root else []

        in_order = in_order_traversal(root)

        def find_misplaced_elements(nums):
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    # first swap occurence
                    if x == -1:
                        x = nums[i]
                    # second swap occurence
                    else:
                        break
            return x, y

        x, y = find_misplaced_elements(in_order)
        print(x, y)

        def dfs(root, x, y, count = 2):
            if not root:
                return
            if (root.val == x or root.val == y) and count > 0:
                root.val = x if root.val == y else y
                count -= 1
            dfs(root.left, x, y, count)
            dfs(root.right, x, y, count)

        dfs(root, x, y)

        print(in_order_traversal(root))

root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)

s = Solution()
s.recoverTree(root)