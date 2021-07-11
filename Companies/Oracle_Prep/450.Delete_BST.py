# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, node: TreeNode, key: int) -> TreeNode:
        if node is None:
            return None
        if node.val == key:
            if not node.right:
                return node.left
            elif not node.left:
                return node.right
            else:
                curr = node.right
                # find the pred
                while curr.left:
                    curr = curr.left
                node.val = curr.val
                node.right = self.deleteNode(node.right, node.val)

        if node.val < key:  # It meaans key would be in the right subtree
            node.right = self.deleteNode(node.right, key)
        else:  # It means key would be in the left subtree
            node.left = self.deleteNode(node.left, key)


s = Solution()
