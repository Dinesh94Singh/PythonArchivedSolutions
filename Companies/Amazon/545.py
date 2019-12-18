"""
545. Boundary of binary tree
"""

# Definition for a binary tree node.


"""
        while (t != null) {
            if (!isLeaf(t)) {
                res.add(t.val);
            }
            if (t.left != null) {
                t = t.left;
            } else {
                t = t.right;
            }

        }
        addLeaves(res, root);
        Stack<Integer> s = new Stack<>();
        t = root.right;
        while (t != null) {
            if (!isLeaf(t)) {
                s.push(t.val);
            }
            if (t.right != null) {
                t = t.right;
            } else {
                t = t.left;
            }
        }
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        left = []
        right = []
        leaves = []

        def is_leaf(root):
            if not root:
                return False
            return not root.left and not root.right

        def find_leaves(root):
            nonlocal leaves
            if root:
                if is_leaf(root):
                    leaves.append(root.val)

                find_leaves(root.left)
                find_leaves(root.right)

        t = root.left
        while t:
            if not is_leaf(t):
                left.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right

        find_leaves(root)

        t = root.right
        while t:
            if not is_leaf(t):
                right.append(t.val)
            if t.right:
                t = t.right
            else:
                t = t.left


        res = [root.val]
        res.extend(left)
        res.extend(leaves)
        res.extend(right)

        return res


'''
Expected Result for below tree => [1, 3, 4, 2]
    1
     \
      2
    /   \
  3      4
'''

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

s = Solution()
print(s.boundaryOfBinaryTree(root))
