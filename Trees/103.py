"""
103. Binary Tree - ZigZag level order traversal

"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zig_zag_level_order(root):
    q = deque([root, ])
    level = 0
    result = []
    while q:
        length = len(q)
        each_level = []
        for _idx in range(length):
            node = q.popleft()
            each_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not level % 2 == 0:
            # odd level, reverse it
            result.append(each_level[::-1])
        else:
            result.append(each_level)
        level += 1
    return result


root = TreeNode(3)
x = root.left = TreeNode(2)
y = root.right = TreeNode(5)
x.left = TreeNode(1)
x.right = TreeNode(3)
y.left = TreeNode(4)
y.right = TreeNode(6)

print(zig_zag_level_order(root))
