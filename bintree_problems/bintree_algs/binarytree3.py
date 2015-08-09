from binarytree import BinaryTreeNode


class BinaryTreeNode3(BinaryTreeNode):
    """Binary tree node with a size parameter"""

    def __init__(self, val=None, left=None, right=None, size=1):
        """Constructs a BinaryTreeNode with a size parameter"""
        self.val = val
        self.left = left
        self.right = right
        self.size = size

    def setleft(self, val=None):
        """Creates a node and sets it as the left child to self."""
        self.left = BinaryTreeNode3(val=val)
        return self.left

    def setright(self, val=None):
        """Creates a node and sets it as the right child to self."""
        self.right = BinaryTreeNode3(val=val)
        return self.right

    def fixsize(self):
        """Goes through the tree recursively to fix the size parameter of
        the nodes."""

        BinaryTreeNode3._fixsize(self)

    @staticmethod
    def _fixsize(node):
        """Recursive helper for fixsize()"""
        if not node:
            return 0
        else:
            node.size = (
                1 + BinaryTreeNode3._fixsize(node.left) +
                BinaryTreeNode3._fixsize(node.right))
            return node.size

    def find_kth_node(self, k):
        """Find the kth node in the tree, i.e. find the kth node that appears
        in the in-order traversal."""
        if self.size < k:
            raise IndexError("There aren't k values in this tree")

        curr = self
        while curr and k:
            if curr.left:
                leftsize = curr.left.size
            else:
                leftsize = 0

            if leftsize < k-1:
                k -= (leftsize + 1)
                curr = curr.right
            elif leftsize is k-1:
                return curr
            else:
                curr = curr.left
