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
    
    def __str__(self):
        print(self.val, self.left, self.right)

class Solution_With_Succ_Pred:
    def successor(self, node: TreeNode) -> TreeNode:
        n = node.right
        while n.left:
            n = n.left
        return n.val
    
    def predecessor(self, node: TreeNode)  -> TreeNode:
        n = node.left
        while n.right:
            n = n.right
        return n.val

    def delete_node(self, root, key):
        if not root: return None

        if root.val > key:
            root.left = self.delete_node(root.left, key)
        elif root.val < key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                del root
                return None
            elif root.right:
                succ = self.successor(root)
                root.val = succ
                root.right = self.delete_node(root.right, root.val)
            else:
                pred = self.predecessor(root)
                root.val = pred
                root.left = self.delete_node(root.left, root.val)
        return root   

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root
        if key<root.val:
            root.left= self.deleteNode(root.left,key)
            return root
        elif key>root.val:
            root.right= self.deleteNode(root.right,key)
            return root
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                cur=root.right
                while cur.left:
                    cur=cur.left
                root.val=cur.val
                root.right=self.deleteNode(root.right,root.val)
                return root

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

s = Solution()
s.deleteNode(root, 3)
print(root)