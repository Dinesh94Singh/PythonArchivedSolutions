"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

"""
Thought Process:
Will doing an inorder traversal verify that it is sorted ?? - No
1. Left subtree will always have a max of root
"""


class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MySolution:
    def __init__(self):
        self.ans = []

    def isValidBst(self, node):
        return self.is_valid_bst(node)

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            self.ans.append(root.val)
            self.in_order_traversal(root.right)
        return self.ans

    def is_valid_bst(self, node):
        if not node:
            return True
        self.in_order_traversal(node)
        for i in range(1, len(self.ans)):
            if not self.ans[i - 1] < self.ans[i]:
                return False
        return True


class LeetCodeSolution:
    def helper(self, node, lower=float("-inf"), upper=float("inf")):
        if node is None:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        return self.helper(node.right, val, upper) and self.helper(
            node.left, lower, val
        )

    def recursive_solution(self, root):
        if root is None:
            return True
        return self.helper(root)

    def iterative_solution(self, root):
        if root is None:
            return True
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, lower, upper = stack.pop()
            if node is None:
                continue
            val = node.val
            if val <= lower or val >= upper:
                return False
            stack.append((node.right, val, upper))
            stack.append((node.left, lower, val))
        return True

    def in_order_solution(self, root):
        """
        TC - O(N) Solution
        SC - O(N) Solution
        """
        if root is None:
            return True
        stack = []
        prev = float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
