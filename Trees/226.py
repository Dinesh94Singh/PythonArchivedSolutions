"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invert_tree_recursion(self, root):
        def helper(node):
            if not node:
                return None
            left, right = node.left, node.right
            node.left = helper(right)
            node.right = helper(left)
            return node

        return helper(root)

    def invert_tree_iterative(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


root = Tree(4)
root.left = Tree(2)
root.right = Tree(7)
root.left.left = Tree(1)
root.left.right = Tree(3)
root.right.left = Tree(6)
root.right.right = Tree(9)

s = Solution()

inverted_root = s.invert_tree_recursion(root)
