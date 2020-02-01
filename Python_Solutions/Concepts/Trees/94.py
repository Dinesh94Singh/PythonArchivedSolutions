"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


res = []
def in_order_traversal_recursive(root):
    if root is None:
        return None
    in_order_traversal_recursive(root.left)
    res.append(root.val)
    in_order_traversal_recursive(root.right)


def in_order_traversal(root):
    stack = []
    curr = root
    res = []
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)


print(in_order_traversal(root))
in_order_traversal_recursive(root)
print(res)
