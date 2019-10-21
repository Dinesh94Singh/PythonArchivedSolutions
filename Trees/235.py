"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Follow Up: What is Binary Tree
"""


class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor_bst(self, root, v1, v2):
        if root is None:
            return None
        val = root.val
        if (v1 < val and v2 > val) or (v1 > val and v2 < val):
            return root
        if v1 == val or v2 == val:
            return root
        if v1 < val and v2 < val:
            return self.lowest_common_ancestor_bst(root.left, v1, v2)
        else:
            return self.lowest_common_ancestor_bst(root.right, v1, v2)


s = Solution()
root = Tree(6)
root.left = Tree(2)
root.right = Tree(8)
root.left.left = Tree(0)
root.left.right = Tree(4)
root.right.left = Tree(7)
root.right.right = Tree(9)
# root = Tree(2)
# root.left = Tree(1)
# root.right = Tree(3)

# print(s.lowest_common_ancestor_bst(root, 3, 1).val)
#  print(s.lowest_common_ancestor_bst(root, 2, 4).val)
print(s.lowest_common_ancestor_bst(root, 2, 8).val)
