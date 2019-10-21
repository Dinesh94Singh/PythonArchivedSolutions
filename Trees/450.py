"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_successor(root):
    node = root.right
    while node:
        node = node.left
    return node.val


def get_predecessor(root):
    node = root.left
    while node:
        node = node.right
    return node.val


def delete_node(root, key):
    if root is None:
        return None
    if root.val < key:
        root.right = delete_node(root.right, key)
    elif root.val > key:
        root.left = delete_node(root.left, key)
    else:
        if not root.left and not root.right:
            # del root
            root = None
        elif root.right:
            root.val = get_successor(root)
            root.right = delete_node(root.right, root.val)  # remove the same node with same value
        else root.left:
            root.val = get_predecessor(root)
            root.left = delete_node(root.left, root.val)
    return root
