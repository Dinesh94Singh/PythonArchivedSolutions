import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def rec_helper(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            return root1.val == root2.val and rec_helper(root1.left, root2.left) and rec_helper(root1.right, root2.right)
        
        return rec_helper(p, q)

    def isSameTree_Iterative(self, p: TreeNode, q: TreeNode) -> bool:
        dq = collections.deque([p, q])

        while dq:
            node1 = dq.popleft()
            node2 = dq.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False
            
            dq.append(node1.left)
            dq.append(node2.left)
            dq.append(node1.right)
            dq.append(node2.right)

        return True

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(1)

root2 = TreeNode(1)
root2.left = TreeNode(1)
root2.right = TreeNode(2)

s = Solution()
print(s.isSameTree_Iterative(root1, root2))