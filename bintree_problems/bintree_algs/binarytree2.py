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
        nextnode = None
        array = []
        while curr:
            if not prev or prev.left is curr or prev.right is curr:
                # if there is no previous, or previous is the parent of curr
                if curr.left:
                    nextnode = curr.left
                else:
                    array.append(curr.val)
                    if curr.right:
                        nextnode = curr.right
                    else:
                        nextnode = curr.parent
            elif curr.left is prev:
                array.append(curr.val)
                if curr.right:
                    nextnode = curr.right
                else:
                    nextnode = curr.parent
            else:
                nextnode = curr.parent
            prev = curr
            curr = nextnode
        return array

    def preordertraversal(self):
        """Returns a string containing the pre order traversal of the root."""
        curr = self
        prev = None
        nextnode = None
        array = []
        while curr:
            if not prev or prev.left is curr or prev.right is curr:
                # if there is no previous, or previous is the parent of curr
                array.append(curr.val)

                if curr.left:
                    nextnode = curr.left
                elif curr.right:
                    nextnode = curr.right
                else:
                    nextnode = curr.parent
            elif curr.left is prev:
                if curr.right:
                    nextnode = curr.right
                else:
                    nextnode = curr.parent
            else:
                nextnode = curr.parent
            prev = curr
            curr = nextnode

        return array

    def postordertraversal(self):
        """Returns a string containing the post order traversal of the root."""
        curr = self
        prev = None
        nextnode = None
        array = []
        while curr:
            if not prev or prev.left is curr or prev.right is curr:
                # if there is no previous, or previous is the parent of curr
                if curr.left:
                    nextnode = curr.left
                elif curr.right:
                    nextnode = curr.right
                else:
                    array.append(curr.val)
                    nextnode = curr.parent
            elif curr.left is prev:
                if curr.right:
                    nextnode = curr.right
                else:
                    array.append(curr.val)
                    nextnode = curr.parent
            else:
                array.append(curr.val)
                nextnode = curr.parent
            prev = curr
            curr = nextnode

        return array
