"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:
==========
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:
==========
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        found = False
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            if not stack:
                return None

            node = stack.pop()
            
            if found:
                return node.val
            
            if node.val == p.val:
                found = True
                
            root = node.right
    
    def inorderSuccessor_optimized_iterative(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # instead of iterating everything, cut
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
            
                
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

find = TreeNode(1)
s = Solution()
print(s.inorderSuccessor(root, find))
print(s.inorderSuccessor_optimized_iterative(root, find).val)