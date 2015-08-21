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


if __name__ == "__main__":
    from node import Node
    from numpy import random as rand
    rand.seed(0)
    testsize = 100
    for ind in xrange(testsize):
        """Test when this the tree is not a real BST."""
        size = rand.randint(50)
        root = Node(key=rand.randint(-50, 50))
        for ind in xrange(size):
            root.add(Node(rand.randint(-10, 10)))
        if not verifyBST(root):
            print "FAIL"

    # Needs a way to verify no false positives.
