"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""

from typing import List
import bisect
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # O(n) sol
    def closestKValues_with_inorder(self, root: TreeNode, target: float, k: int) -> List[int]:
        """
            O(N) solution -> Perform In-order traversal -> in the second pass, find the idx, where the target is best suited for, go left and right until k becomes 0 (Easy)

            Follow-up: Less than O(n) means, not visiting all the nodes -> Hard (Might have to do it binarily
        """
        def inorder(root):
            nonlocal in_order
            if not root:
                return
            inorder(root.left)
            in_order.append(root.val)
            inorder(root.right)

        in_order = []
        inorder(root)

        idx = bisect.bisect_left(in_order, target)
        if idx == len(in_order):
            left, right = idx - 1, idx
        elif idx >= 1 and in_order[idx] > in_order[idx - 1]:
            left, right = idx - 1, idx
        else:
            left, right = idx, idx + 1
        res = []
        while (0 <= left or right < len(in_order)) and k:
            if not 0 <= left:
                res.append(in_order[right])
                right += 1
            elif not right < len(in_order):
                res.append(in_order[left])
                left -= 1
            else:
                diff1 = abs(in_order[left] - target)
                diff2 = abs(in_order[right] - target)

                if diff1 < diff2:
                    res.append(in_order[left])
                    left -= 1
                else:
                    res.append(in_order[right])
                    right += 1
            k -= 1

        return res

    def closestKValues_with_2_stacks(self, root: TreeNode, target: float, k: int) -> List[int]:
        pass

    # O(klogn) -> Problem when height of the tree is too large (if height of the tree > total number of elements)
    def closestKValues_with_pq(self, root: TreeNode, target: float, k: int) -> List[int]:
        def helper(heap, target):
            _, head, flag = heapq.heappop(heap)
            curr = head.left if not flag else head.right
            while curr:
                heapq.heappush(heap, (abs(curr.val - target), curr, flag))
                curr = curr.right if not flag else curr.left
            return head.val
        heap, res = [], []
        while root:
            flag = 0 if root.val < target else 1
            heapq.heappush(heap, (abs(root.val - target), root, flag)) # min_heap will have the closest value in the top. When you heapop, you will only get the
            root = root.left if flag else root.right
        for _ in range(k):
            res.append(helper(heap, target))
        return res

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

s = Solution()
print(s.closestKValues_with_inorder(root, 3.7, 2)) # [4, 3]
print(s.closestKValues_with_pq(root, 3.7, 2))

print('\n\n')

root = TreeNode(1)
print(s.closestKValues_with_inorder(root, 4.428571, 1)) # [1]
print(s.closestKValues_with_pq(root, 4.42, 1))

print('\n\n')

root = TreeNode(2)
root.left = TreeNode(1)
print(s.closestKValues_with_inorder(root, 2147483647.0, 1)) # [2]
print(s.closestKValues_with_pq(root, 2147483647.0, 1)) # [2]

print('\n\n')

root = TreeNode(1)
root.right = TreeNode(8)
print(s.closestKValues_with_inorder(root, 3.0, 1)) # [1]
print(s.closestKValues_with_pq(root, 3.0, 1)) # [1]
