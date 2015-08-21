def findsuccessor(node):
    """Finds the successor of a node in a BST. Uses parent pointers."""
    # If there is a right child, return smallest element in the right tree.
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    # No right child. Walk up until node is a left child.
    while node.parent and node.parent.right and node.parent.right == node:
        node = node.parent
    return node.parent  # If None is returned, then the root was reached.
