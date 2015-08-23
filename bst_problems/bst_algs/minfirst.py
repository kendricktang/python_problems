def findk(root, k):
    """Root is a min-first BST, i.e. root.val is less than all keys,
    and all keys in the left tree are less than all keys in the right tree.

    Returns True if k is in the tree. Otherwise returns False or None"""
    if not root:
        return False
    if root.key == k:
        return True
    if root.key > k:
        return False

    curr = root
    while curr and curr.key < k:
        if curr.right and k < curr.right.key:
            curr = curr.left
        elif curr.right:
            # curr.right.key < k
            curr = curr.right
        else:
            # curr.right doesn't exist
            curr = curr.left

    return curr and curr.key == k
