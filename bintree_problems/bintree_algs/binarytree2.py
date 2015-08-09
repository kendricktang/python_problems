from binarytree import BinaryTreeNode


class BinaryTreeNode2(BinaryTreeNode):
    """Binary tree node with a parent pointer"""

    def __init__(self, val=None, left=None, right=None, parent=None):
        """Constructs a binary tree node with a parent pointer."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def setleft(self, val=None):
        """Creates a node and sets the left child to that value."""
        self.left = BinaryTreeNode2(
            val=val, left=None, right=None, parent=self)
        return self.left

    def setright(self, val=None):
        """Creates a node and sets the right child to that value."""
        self.right = BinaryTreeNode2(
            val=val, left=None, right=None, parent=self)
        return self.right

    def inordertraversal(self):
        """Returns a string containing the in order traversal of the root."""
        curr = self
        prev = None
        next = None
        s = ''
        while curr:
            if not prev or prev.left is curr or prev.right is curr:
                # if there is no previous, or previous is the parent of curr
                if curr.left:
                    next = curr.left
                else:
                    s += str(curr.val)
                    s += ","
                    if curr.right:
                        next = curr.right
                    else:
                        next = curr.parent
            elif curr.left is prev:
                s += str(curr.val)
                s += ","
                if curr.right:
                    next = curr.right
                else:
                    next = curr.parent
            else:
                next = curr.parent
            prev = curr
            curr = next
        if s[-1] is ",":
            return s[:-1]
        return s

    def preordertraversal(self):
        """Returns a string containing the pre order traversal of the root."""
        curr = self
        prev = None
        next = None
        s = ''
        while curr:
            if not prev or prev.left is curr or prev.right is curr:
                # if there is no previous, or previous is the parent of curr
                s += str(curr.val)
                s += ","

                if curr.left:
                    next = curr.left
                elif curr.right:
                    next = curr.right
                else:
                    next = curr.parent
            elif curr.left is prev:
                if curr.right:
                    next = curr.right
                else:
                    next = curr.parent
            else:
                next = curr.parent
            prev = curr
            curr = next

        if s[-1] is ",":
            return s[:-1]
        return s

    def postordertraversal(self):
        """Returns a string containing the post order traversal of the root."""
        curr = self
        prev = None
        next = None
        s = ''
        while curr:
            if not prev or prev.left is curr or prev.right is curr:
                # if there is no previous, or previous is the parent of curr
                if curr.left:
                    next = curr.left
                elif curr.right:
                    next = curr.right
                else:
                    s += str(curr.val)
                    s += ","
                    next = curr.parent
            elif curr.left is prev:
                if curr.right:
                    next = curr.right
                else:
                    s += str(curr.val)
                    s += ","
                    next = curr.parent
            else:
                s += str(curr.val)
                s += ","
                next = curr.parent
            prev = curr
            curr = next

        if s[-1] is ",":
            return s[:-1]
        return s
