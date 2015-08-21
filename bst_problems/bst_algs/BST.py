from node import Node

class BinarySearchTree(Node):
    """A BST which does not contain duplicate keys."""

    def __init__(self):
        """Initializes an empty BST."""
        self.root = None

    def empty(self):
        """Returns True if BST is empty. False otherwise."""
        return not self.root

    def clear(self):
        """Recursively deletes a node's pointers to children and
        the node iteself."""
        BinarySearchTree._clear(self.root)

    @staticmethod
    def _clear(node):
        """Recursive helper for clear."""
        if node:
            BinarySearchTree._clear(node.left)
            BinarySearchTree._clear(node.right)
            node = None

    def add(self, key):
        """Treating self as a root of a BST, adds a node with node.key=key
        to the tree if key does not already exist in the tree.
        The root (self) must be the root of a tree which does not contain
        duplicates."""

        newnode = Node(key)
        if self.empty():
            self.root = newnode
        else:
            curr = self.root
            while curr:
                parent = curr
                if curr.key == key:
                    # Key already existed. No add is done.
                    return False
                elif key < curr.key:
                    curr = curr.left
                else:
                    curr = curr.right

            if key < parent.key:
                parent.left = newnode
            else:
                parent.right = newnode
        return True

    def remove(self, key):
        """Treating self as a root of a BST, removes the node with node.key=key
        from the tree if that node exists.
        The root (self) must be the root of a tree which does not contain
        duplicates."""
        curr = self.root
        # Find the key in the tree.
        while curr and curr.key != key:
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:
            # Key was not present in the tree.
            return False

        if curr.right:
            # curr has a right tree. Find min key in right tree.
            right_curr = curr.right
            right_parent = curr
            while right_curr.left:
                right_parent = right_curr
                right_curr = right_curr.left
            # right_curr has the smallest key. Reorder tree here.
            Node.replaceparentchildlink(parent, curr, right_curr)
            Node.replaceparentchildlink(
                right_parent, right_curr, right_curr.right)
            right_curr.right = curr.right
            right_curr.left = curr.left

            if self.root == curr:
                self.root = right_curr
        else:
            # curr doesn't have a right tree. Replace curr with curr.left.
            if self.root == curr:
                self.root = curr.left
            Node.replaceparentchildlink(parent, curr, curr.left)
        curr = None
        return True
