class BinaryTreeNode(object):
    """A binary tree node. No parent pointer. No sorting restriction."""

    def __init__(self, val=None, left=None, right=None):
        """Creates an ordinary binary tree node object."""
        self.val = val
        self.left = left
        self.right = right

    def setleft(self, val=None):
        """Creates a node and sets it as the left child of self."""
        self.left = BinaryTreeNode(val=val)
        return self.left

    def setright(self, val=None):
        """Creates a node and sets it as the left child of self."""
        self.right = BinaryTreeNode(val=val)
        return self.right

    def inordertraversal(self):
        """Returns a string representing the in-order traversal of this tree."""
        curr = self
        array = []
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right and pre.right is not curr:
                    pre = pre.right

                if pre.right:
                    pre.right = None
                    array.append(curr.val)
                    curr = curr.right
                else:
                    pre.right = curr
                    curr = curr.left

            else:
                array.append(curr.val)
                curr = curr.right
        return array

    def isbalanced(self):
        """Determines if the tree is balanced. A tree is balanced if the height
        of its left child and the height of its right child differs by at most
        one."""
        height = BinaryTreeNode._isbalanced(self)
        return height is not -1

    @staticmethod
    def _isbalanced(node):
        """Recursive helper for isbalanced()."""
        if not node:
            return 0

        leftheight = BinaryTreeNode._isbalanced(node.left)
        if leftheight is -1:
            return -1

        rightheight = BinaryTreeNode._isbalanced(node.right)
        if rightheight is -1:
            return -1

        if abs(leftheight - rightheight) > 1:
            return -1

        return max(leftheight, rightheight) + 1

    def findkunbalanceddescendent(self, k):
        """Returns the first (in an in-order traversal) node which is not
        k-balanced. A node is k-balanced if the number of nodes in its left
        branch and the number of nodes in its right branch differ by at most k.
        """
        numofnodes, unbalancednode = (
            BinaryTreeNode._findkunbalanceddescendent(self, k))
        return unbalancednode

    @staticmethod
    def _findkunbalanceddescendent(node, k):
        """Recursive helper for findkunbalanceddescendent()."""
        if not node:
            return 0, None

        leftsize, unbalancednode = (
            BinaryTreeNode._findkunbalanceddescendent(node.left, k))
        if unbalancednode:
            return 0, unbalancednode

        rightsize, unbalancednode = (
            BinaryTreeNode._findkunbalanceddescendent(node.right, k))
        if unbalancednode:
            return 0, unbalancednode

        if abs(leftsize - rightsize) > k:
            return 0, node

        return leftsize + rightsize + 1, None

    def issymmetric(self):
        """Determines whether the tree is symmetric."""
        return BinaryTreeNode._issymmetric(self.left, self.right)

    @staticmethod
    def _issymmetric(leftside, rightside):
        """Recursive helper for issymmetric()."""
        if not leftside and not rightside:
            return True

        return (
            leftside and rightside and
            leftside.val is rightside.val and
            BinaryTreeNode._issymmetric(leftside.left, rightside.right) and
            BinaryTreeNode._issymmetric(leftside.right, rightside.left))
