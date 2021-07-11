# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __del__(self):
        print('deleted', self.val)


from typing import List

"""
Brute Force: During Each pass, store the information of parent and if its the left or right node, which is a leaf
After each pass, get the parent and node info => Mark the node as none. During the last pass, if parent is none => Mark the node as None
T.C: O(N^K) - Since we are looping K times
"""

"""
Two Pass Solution - Find the height during the first pass, during the second pass, find how far is it from the leaf - Max Far dist, is the idx where we want to add the res
"""
class Two_Pass_Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def find_height(root):
            if not root: return 0
            left = find_height(root.left)
            right = find_height(root.right)
            return max(left, right) + 1
        
        height = find_height(root)
        print(height)

        res = [[] for _ in range(height)]

        def find_leaves(root):
            if not root:
                return 0

            left_dist = find_leaves(root.left)
            right_dist = find_leaves(root.right)

            idx = max(left_dist, right_dist)
            res[idx].append(root.val)
            return idx + 1



        find_leaves(root)
        return res


class Single_Pass_Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        def find_leaves(root):
            if not root:
                return 0

            left_dist = find_leaves(root.left)
            right_dist = find_leaves(root.right)

            idx = max(left_dist, right_dist)
            if len(res) > idx:
                res[idx].append(root.val)
            else:
                res.append([])
                res[idx].append(root.val)

            return idx + 1



        find_leaves(root)
        return res

class delete_nodes_Solution:
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
            res = []
            def find_leaves(root):
                if not root:
                    return 0

                left_dist = find_leaves(root.left)
                right_dist = find_leaves(root.right)

                idx = max(left_dist, right_dist)
                if len(res) > idx:
                    res[idx].append(root.val)
                else:
                    res.append([])
                    res[idx].append(root.val)
                
                del root

                return idx + 1

            find_leaves(root)
            return res

class BFS_Solution:
    """
    * Intution: Do a topological sort - as the inorder becomes, initially level 0 => next => level 1
    * For deletion of nodes, when you pop => Delete the address location of the node.
    """
    pass

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

two_pass = Two_Pass_Solution()
print(two_pass.findLeaves(root))

single_pass = Single_Pass_Solution()
print(single_pass.findLeaves(root))


delete_nodes_Solution = delete_nodes_Solution()
print(delete_nodes_Solution.findLeaves(root))
print(delete_nodes_Solution.inorder(root))
