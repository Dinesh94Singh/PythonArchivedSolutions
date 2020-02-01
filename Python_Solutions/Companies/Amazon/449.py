"""

449. Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized
 to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should
be stateless.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def post_order(root):
            return post_order(root.left) + post_order(root.right) + [root.val] if root else []

        return ' '.join(map(str, post_order(root)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        post_order = [int(each) for each in data.split(' ') if data]
        print(post_order)

        def helper(lower=float('-inf'), upper=float('inf')):
            if not post_order or post_order[-1] < lower or post_order[-1] > upper:
                return None
            val = post_order.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)

            return root

        r = helper()
        return r

# Your Codec object will be instantiated and called as such:
root = TreeNode(5)
root.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(7)
root.right.left = TreeNode(6)

codec = Codec()
codec.deserialize(codec.serialize(root))

