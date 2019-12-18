"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


class Solution:
    BOTH_PENDING = 2
    LEFT_DONE = 1
    RIGHT_DONE = 0

    def lowest_common_ancestor_binary_tree_recursion(self, root, v1, v2):
        def helper(node):
            if node is None:
                return False

            left = helper(node.left)
            right = helper(node.right)
            mid = node == v1 or node == v2

            if mid + left + right >= 2:  # True = 1, False = 0
                self.ans = node

            return mid or left or right

        helper(root)
        return self.ans

    def lowest_common_ancestor_binary_tree_iteration(self, root, v1, v2):
        stack = [root]  # to do bfs
        parent = {root: None}
        while v1 not in parent or v2 not in parent:
            # Loop till v1 and v2 are both in parent
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        # add all v1's ancestors along with v1 till root.
        while v1:
            ancestors.add(v1)
            v1 = parent[v1]
        # if v2 is child of v1, then ancestors would already have v1
        while v2 not in ancestors:
            v2 = parent[v2]
        return v2
