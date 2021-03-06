class Node(object):
    """A binary search tree node object. The nodes will have a value, in
    addition to multiple pointers (e.g. parent) or parameters (e.g. size).
    Not all of which will be used everytime, but I don't want to make a
    different Node class for each problem.
    """
    def __init__(self, key=None, parent=None, left=None, right=None):
        """Constructs a BST node."""
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def add(self, other, parent=False):
        """Treating self as a root of a BST, add(other) will place other in
        a legal spot of the BST."""
        curr = self
        prev = None
        while curr:
            prev = curr
            if other.key <= curr.key:
                curr = curr.left
            else:
                curr = curr.right
        if other.key <= prev.key:
            prev.left = other
            if parent:
                other.parent = prev
        else:
            prev.right = other
            if parent:
                other.parent = prev

    def inordertraversal(self):
        return Node._inordertraversal(self)

    @staticmethod
    def _inordertraversal(curr):
        """Returns an array representing the in-order traversal of a tree."""
        if not curr:
            return []
        return (
            Node._inordertraversal(curr.left) +
            [curr.key] + Node._inordertraversal(curr.right))

    @staticmethod
    def replaceparentchildlink(parent, child, newnode):
        """Replaces the link between a parent and a child with a new node.
        If the child is not the child of parent, does nothing."""
        if not parent:
            return

        if parent.left == child:
            parent.left = newnode
        elif parent.right == child:
            parent.right = newnode

    @staticmethod
    def getheight(node):
        """Returns the height of a node. Leaves have height 0."""
        if not node:
            return -1
        return 1 + max(Node.getheight(node.right), Node.getheight(node.left))
