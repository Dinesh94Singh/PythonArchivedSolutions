"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary Tree defined as a binary Tree which the depth of the two subTree
every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""


# Definition for a binary Tree.
class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sorted_array_to_bst(self, nums):
        def helper(left, right):
            # print('left is', left, 'right is', right)
            if left >= right:
                return
            mid = (left + right) // 2
            node = Tree(nums[mid])
            node.left = helper(left, mid)
            node.right = helper(mid + 1, right)
            return node

        return helper(0, len(nums))

"""
This is wrong apporach - redo
"""
    def sorted_array_to_bst_iterative(self, nums):
        root = Tree(0)
        stack = [(root, 0, len(nums) - 1)]
        while stack:
            node, left, right = stack.pop()
            # creating node is not possible in the loop because, you don't know if its a left / right sub tree
            if left >= right:
                continue
            mid = (left + right) // 2
            # print('left', left, 'right', right, 'mid', mid)
            node.val = nums[mid]

            if left < mid:
                node.left = Tree(0) # creating 0's would result in extra nodes
                stack.append((node.left, left, mid))
            if right > mid:
                node.right = Tree(0)
                stack.append((node.right, mid + 1, right))
        return root

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            res.append(root.val)
            self.in_order(root.right)

res = []
s = Solution()
root = s.sorted_array_to_bst([1, 7, 9, 11, 15, 17, 66, 88])
root = s.sorted_array_to_bst_iterative([1, 7, 9, 11, 15, 17, 66, 88])
s.in_order(root)
print(res)
