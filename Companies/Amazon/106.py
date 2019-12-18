"""
Given postorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

postorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorder_traversal(self, root):
        if not root:
            return
        print(root.val, end='\t')
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)

    def buildTree(self, inorder, postorder):
        def helper(in_order, post_order):
            if len(in_order) == 0:
                return None

            idx = 0
            found = False
            for root in reversed(post_order):
                for index, each in enumerate(in_order):
                    if each == root:
                        found = True
                        idx = index
                        break
                if found:
                    break
            r = TreeNode(root)
            if len(in_order) == 1:
                pass
            else:
                postorder_length = len(post_order)
                r.left = helper(in_order[:idx], post_order[: postorder_length - 1])
                r.right = helper(in_order[idx + 1:], post_order[: postorder_length - 1])
            return r

        return helper(inorder, postorder)


s = Solution()
root = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]);
# root = s.buildTree([1, 2], [2, 1]);
s.postorder_traversal(root)
