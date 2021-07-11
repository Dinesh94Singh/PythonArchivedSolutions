# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def __init__(self):
        self.numOfPaths = 0

    def pathSum(self, root, target):
        self.dfs(root, target)
        return self.numOfPaths

    def dfs(self, node, target):
        # exit condition
        if node is None:
            return
        self.test(node, target)  # you can move the line to any order, here is pre-order
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1

        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)


class AnotherSolution_Using_Memo:
    def __init__(self):
        self.result = 0

    def pathSum(self, root, target):
        # define global result and path
        cache = {0: 1}

        # recursive to get result
        self.dfs(root, target, 0, cache)

        # return result
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return
            # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1



s = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

s.pathSum(root, 3)
