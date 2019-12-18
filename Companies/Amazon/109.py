"""

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        def get_array(x):
            res = []
            temp = x
            while temp:
                res.append(temp.val)
                temp = temp.next
            return res

        def convert_to_bst(l, r, values):
            if l > r:
                return None

            mid = (l + r) // 2

            node = TreeNode(values[mid])

            if l == r:  # only one element left in the array
                return node

            node.left = convert_to_bst(l, mid - 1, values)
            node.right = convert_to_bst(mid + 1, r, values)

            return node

        values = get_array(head)
        return convert_to_bst(0, len(values) - 1, values)

    def sortedListToBST_InorderApproach(self, head):
            def findSize(head):
                ptr = head
                c = 0
                while ptr:
                    ptr = ptr.next
                    c += 1
                return c

            def sortedListToBST(head):
                """
                :type head: ListNode
                :rtype: TreeNode
                """

                # Get the size of the linked list first
                size = findSize(head)

                # Recursively form a BST out of linked list from l --> r
                def convert(l, r):
                    nonlocal head

                    # Invalid case
                    if l > r:
                        return None

                    mid = (l + r) // 2

                    # First step of simulated inorder traversal. Recursively form
                    # the left half
                    left = convert(l, mid - 1)

                    # Once left half is traversed, process the current node
                    node = TreeNode(head.val)
                    node.left = left

                    # Maintain the invariance mentioned in the algorithm
                    head = head.next

                    # Recurse on the right hand side and form BST out of them
                    node.right = convert(mid + 1, r)
                    return node

                return convert(0, size - 1)

[-10,-3,0,5,9],

head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)