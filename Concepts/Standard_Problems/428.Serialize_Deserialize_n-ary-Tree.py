# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        order = []

        def pre_order(root):
            if not root:
                return None
            order.append(root.val)
            for each_child in root.children:
                pre_order(each_child)
            order.append('#')  # indicates the end of the branch

        pre_order(root)
        return ','.join(order)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data is None or data == '':
            return None
        data = data.split(',')
        stack = []
        for each in data[:-1]:
            if each == '#':
                node = stack.pop()
                stack[-1].children.append(node)
            else:
                stack.append(Node(int(each), []))

        return stack[0]


# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.deserialize(codec.serialize(root))
