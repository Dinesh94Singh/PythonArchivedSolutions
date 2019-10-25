# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root):
            if not root:
                return 0
            if (p < root.val < q) or (p > root.val > q) or root.val == p or root.val == q:
                return root
            if p > root.val and q > root.val:
                # inside right subtree
                return dfs(root.right)
            if p < root.val and q < root.val:
                # inside left subtree
                return dfs(root.left)
        return dfs(root)
    def dist_bw_nodes(self, root, p, q):
        lca = self.lowestCommonAncestor(root, p, q)
        dist1, dist2 = 0, 0
        def dfs(root, level_from_root):
            nonlocal dist1, dist2
            if not root:
                return
            if root.val == p:
                dist1 = level_from_root
            if root.val == q:
                dist2 = level_from_root
            if dist1 != 0 and dist2 != 0:
                return
            return dfs(root.left, level_from_root + 1) or dfs(root.right, level_from_root + 1)
        dfs(lca, 0)
        return dist1 + dist2

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

s = Solution()
s.lowestCommonAncestor(root, 2, 8)
s.lowestCommonAncestor(root, 4, 3)
s.lowestCommonAncestor(root, 6, 2)
# s.lowestCommonAncestor(root, 1, 3)

print(s.dist_bw_nodes(root, 2, 8))
print(s.dist_bw_nodes(root, 0, 9))
print(s.dist_bw_nodes(root, 2, 5))
