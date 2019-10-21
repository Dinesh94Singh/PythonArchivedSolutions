"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_symmetric(root):
    def mirror(left, right):
        if left is None and right is None:
            return True
        if (left is None and right is not None) or (left is not None and right is None):
            return False
        return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)
    if root is None:
        return True
    return mirror(root.left, root.right)


def is_symmetric_iterative(root):
    q = []
    q.append(root.left)
    q.append(root.right)
    while q:
        n1 = q.pop()
        n2 = q.pop()
        if not n1 and not n2:
            continue
        if not n1 or not n2:
            return False
        if n1.val != n2.val:
            return False
        q.append(n1.left)
        q.append(n2.right)
        q.append(n1.right)
        q.append(n2.left)
    return True

root = TreeNode(1)
x = root.left = TreeNode(2)
y = root.right = TreeNode(2)
x.left = TreeNode(3)
x.right = TreeNode(4)
y.left = TreeNode(4)
y.right = TreeNode(3)

print(is_symmetric(root))