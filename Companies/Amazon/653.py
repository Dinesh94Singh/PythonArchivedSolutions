# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            in_order.append(root.val)
            inorder(root.right)

        in_order = []
        inorder(root)
        print(in_order)
        hm = {}

        def twoSum(in_order, target):
            for i in range(len(in_order)):
                print(hm, in_order[i])
                if in_order[i] in hm:
                    return True
                elif in_order[i] == None:
                    continue
                else:
                    hm[target - in_order[i]] = i
            # return False

        twoSum(in_order, k)

"""
    5
   / \
  3   6
 / \   \
2   4   7

"""
        
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

s = Solution()
print(s.findTarget(root, 9))