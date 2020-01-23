# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        post_order = []
        def rserialize(root):
            if not root:
                post_order.append('None')
                return
            rserialize(root.left)
            rserialize(root.right)
            post_order.append(root.val)
            
        rserialize(root)
        
        return ','.join(map(str, post_order))
        
        

    def deserialize(self, data):
        post_order = data.split(',')
        def dserialize(post_order):
            if not post_order:
                return None
            val = post_order.pop()
            
            if val == 'None':
                return None
            
            root = TreeNode(int(val))
            root.right = dserialize(post_order)
            root.left = dserialize(post_order)

            return root
            
        return dserialize(post_order)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

c = Codec()
data = c.serialize(root)
print(data)
new_root = c.deserialize(data)
print(c.serialize(new_root))