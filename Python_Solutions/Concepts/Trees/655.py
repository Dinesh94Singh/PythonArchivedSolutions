from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def find_depth_tree(root):
            if not root:
                return 0
            left = find_depth_tree(root.left)
            right = find_depth_tree(root.right)
            return max(left, right) + 1

        depth = find_depth_tree(root)
        print(depth)

        grid = [['' for _ in range(2 ** depth - 1)] for _ in range(depth)]

        def dfs(root, left, right, d):
            nonlocal grid
            if not root:
                return
            mid = (left + right) // 2
            grid[d][mid] = "{}".format(root.val)
            dfs(root.left, left, mid - 1, d + 1)
            dfs(root.right, mid + 1, right, d + 1)

        dfs(root, 0, 2 ** depth - 1, 0)

        return grid


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(4)

root = TreeNode(1)
root.left = TreeNode(2)

s = Solution()
grid = s.printTree(root)

for each_row in grid:
    print(each_row)

