"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree. You may
assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when
next() is called. """


# Definition for a binary tree node.
class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: Tree):
        self.stack = []
        self.push_all(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.has_next():
            next_val = self.stack.pop()
            self.push_all(next_val.right)
            return next_val.val
        else:
            print('There is nothing in the stack')

    def has_next(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) >= 1

    def push_all(self, root):
        while root:
            self.stack.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

root = Tree(7)
root.left = Tree(3)
root.right = Tree(15)
root.right.left = Tree(9)
root.right.right = Tree(20)

itr = BSTIterator(root)

itr.has_next()
itr.next()

itr.has_next()
itr.next()

itr.has_next()
itr.next()

itr.has_next()
itr.next()

itr.has_next()
itr.next()

itr.has_next()
itr.next()
