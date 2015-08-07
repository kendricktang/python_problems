class BinaryTreeNode(object):
    """A binary tree node. No parent pointer. No sorting restriction."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def setleft(self, val):
        self.left = BinaryTreeNode(val)

    def setright(self, val):
        self.right = BinaryTreeNode(val)

    def inordertraversal(self):
        curr = self
        s = ""
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right and pre.right is not curr:
                    pre = pre.right

                if pre.right:
                    pre.right = None
                    s += str(curr.val)
                    curr = curr.right
                    if curr:
                        s += ","
                else:
                    pre.right = curr
                    curr = curr.left

            else:
                s += str(curr.val)
                curr = curr.right
                if curr:
                    s += ","
        return s

    def isbalanced(self):
        height = BinaryTreeNode._isbalanced(self)
        return height is not -1

    @staticmethod
    def _isbalanced(node):
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

    def findkbalanceddescendent(self, k):
        numofnodes, unbalancednode = (
            BinaryTreeNode._findkbalanceddescendent(self, k))
        return unbalancednode

    @staticmethod
    def _findkbalanceddescendent(node, k):
        if not node:
            return 0, None

        leftheight, unbalancednode = (
            BinaryTreeNode._findkbalanceddescendent(node.left, k))
        if unbalancednode:
            return 0, unbalancednode

        rightheight, unbalancednode = (
            BinaryTreeNode._findkbalanceddescendent(node.right, k))
        if unbalancednode:
            return 0, unbalancednode

        if abs(leftheight - rightheight) > k:
            return 0, node

        return leftheight + rightheight + 1, None

    def issymmetric(self):
        return BinaryTreeNode._issymmetric(self.left, self.right)

    @staticmethod
    def _issymmetric(leftside, rightside):
        if not leftside and not rightside:
            return True

        return (
            leftside.val is rightside.val and
            BinaryTreeNode._issymmetric(leftside.left, rightside.right) and
            BinaryTreeNode._issymmetric(leftside.right, rightside.left))
