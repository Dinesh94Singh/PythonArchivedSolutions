"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""

from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

res = []
def level_order_bottom_dfs(root):
    def dfs(root, depth):
        if root is None:
            return
        if len(res) > depth:
            res[depth].append(root.val)
        else:
            res.append([root.val])
        dfs(root.left, depth + 1)
        dfs(root.right, depth + 1)
    dfs(root, 0)
    return res[::-1]

def level_order_bottom_bfs(root):
    q = deque([root, ])
    res = []
    while q:
        n = len(q)
        level_order = []
        for _ in range(n):
            node = q.popleft()
            level_order.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level_order)
    return res[::-1]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

level_order_bottom_bfs(root)
level_order_bottom_dfs(root)
