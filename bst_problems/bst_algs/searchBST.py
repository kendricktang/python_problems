def findfirstk_iterative(root, k):
    """Given the root of a BST (where keys are not necessarily distinct)
    return the "first" Node which contains k, where order is determined
    by an in-order-traversal. This is an iterative approach."""
    curr = root
    # Find a node with key = k.
    while curr and curr.key != k:
        if k < curr.key:
            curr = curr.left
        else:
            curr = curr.right

    # Go left for the "first" node with key k.
    while curr and curr.left and curr.left.key == k:
        curr = curr.left

    # If curr is None, then k is not in the tree.
    return curr


def findfirstk_recursive(node, k, found=False):
    """Given the root of a BST (where keys are not necessarily distinct)
    return the "first" Node which contains k, where order is determined
    by an in-order-traversal. This is a recursive approach."""
    if not node:
        return None
    if node.key == k:
        # Check left tree for more Nodes where node.key is k
        nextnode = findfirstk_recursive(node.left, k, found=True)
        if nextnode:
            return nextnode
        else:
            return node
    elif node.key < k:
        # Check right tree, unless k is already found.
        if found:
            return None
        return findfirstk_recursive(node.right, k)
    else:
        # Check left tree
        return findfirstk_recursive(node.left, k)


def findlargerthank(node, k):
    """Finds the first node with key greater than k.
    "First" is with respect to an in-order-traversal."""
    found = False
    returnnode = None
    curr = node
    while curr:
        if curr.key == k:
            # Found the key, but check the right child for first key > k.
            found = True
            curr = curr.right
        elif curr.key > k:
            returnnode = curr
            curr = curr.left
        else:
            curr = curr.right

    if found:
        return returnnode
    return None
