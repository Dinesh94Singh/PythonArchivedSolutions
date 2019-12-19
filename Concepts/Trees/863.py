"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        res = []

        def find_root(root, target):
            if not root:
                return -1

            if root == target:
                k_depth(target, 0, K)
                return 1

            L = find_root(root.left, target)
            R = find_root(root.right, target)

            if L != -1:
                if L == K:
                    res.append(root.val)
                k_depth(root, L+1, K)
                return L + 1
            elif R != -1:
                if R == K:
                    res.append(root.val)
                k_depth(root, R+1, K)
                return R + 1
            else:
                return -1

        def k_depth(root, depth, k):
            if not root:
                return
            if depth == k:
                res.append(root.val)
            k_depth(root.left, depth + 1, k)
            k_depth(root.right, depth + 1, k)
