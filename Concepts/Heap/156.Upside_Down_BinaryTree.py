# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root):
        if not root: return 

        self.inorder(root.left)
        print(root.val, end=' ')
        self.inorder(root.right)

    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        pass


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

s = Solution()
# s.inorder(root)
s.upsideDownBinaryTree(root)
s.inorder(root)


        