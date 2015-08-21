def verifyBST(root):
    """Verifies whether a binary tree satisfies the BST property."""
    return _verifyBST(root, None, None)


def _verifyBST(root, minkey, maxkey):
    """Recursive helper for verifyBST(). Given minkey and maxkey,
    the left subtree can only contain values within the range [minkey, root.key]
    and the right subtree can only contain values within the range
    [root.key, maxkey]."""
    if not root:
        return True

    if (minkey and root.key < minkey) or (maxkey and root.key > maxkey):
        return False
    else:
        return (
            _verifyBST(root.left, minkey, root.key) and
             _verifyBST(root.right, root.key, maxkey))
