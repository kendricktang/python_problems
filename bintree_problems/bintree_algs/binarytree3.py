from binarytree import BinaryTreeNode


class BinaryTreeNode3(BinaryTreeNode):
    """Binary tree node with a size parameter"""

    def __init__(self, val, left=None, right=None, size=1):
        self.val = val
        self.left = left
        self.right = right
        self.size = size

    def setleft(self, val):
        self.left = BinaryTreeNode3(val)

    def setright(self, val):
        self.right = BinaryTreeNode3(val)

    def fixsize(self):
        BinaryTreeNode3._fixsize(self)

    @staticmethod
    def _fixsize(node):
        if not node.left and not node.right:
            return 0
        else:
            node.size = (
                1 + BinaryTreeNode3._fixsize(node.left) +
                BinaryTreeNode3._fixsize(node.right))
            return node.sizeB

    def find_kth_node(self, k):
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
