"""Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary
includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may
still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root
to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary
or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if
exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].


Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return None

        res = [root.val]
        left = self.find_left_node(root.left)
        right = self.find_right_node(root.right)
        self.leaves = []
        if root.left or root.right:
            self.find_leaves(root)

        res += left + self.leaves + right
        return res

    def is_not_leaf(self, root):
        return root.left or root.right

    def find_left_node(self, root):
        if not root:
            return []
        left = []
        while root and self.is_not_leaf(root):
            left.append(root.val)
            if root.left:
                root = root.left
            else:
                root = root.right
        return left

    def find_right_node(self, root):
        if not root:
            return []
        right = []
        while root and self.is_not_leaf(root):
            right.append(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left
        return right[::-1]

    def find_leaves(self, root):
        if not root.left and not root.right:
            self.leaves.append(root.val)
        if root.left:
            self.find_leaves(root.left)
        if root.right:
            self.find_leaves(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)

s = Solution()
print(s.boundaryOfBinaryTree(root))

print('\n\n')

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

print(s.boundaryOfBinaryTree(root))
