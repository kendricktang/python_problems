def findfirstk_iterative(root, k):
    """Given the root of a BST (where keys are not necessarily distinct)
    return the "first" Node which contains k, where order is determined
    by an in-order-traversal.

    This is an iterative approach."""

    curr = root
    # First step: find a node with key = k.
    while curr and curr.key != k:
        if k < curr.key:
            curr = curr.left
        else:
            curr = curr.right

    # Second step: go left for the "first" node with key k.
    while curr and curr.left and curr.left.key == k:
        curr = curr.left

    # Third step: return curr. If curr is None, then k is not in the tree.
    return curr


def findfirstk_recursive(node, k, found=False):
    """Given the root of a BST (where keys are not necessarily distinct)
    return the "first" Node which contains k, where order is determined
    by an in-order-traversal.

    This is a recursive approach."""
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
        # Check right tree
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
            # Found the key, but search to the right until curr.key > k
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


if __name__ == "__main__":
    from node import Node
    from numpy import random

    random.seed(0)
    size = 500
    testsize = 200
    for ind in xrange(testsize):
        # TESTS WHEN KEY IS IN THE TREE
        root = Node()
        array = []
        for x in xrange(size):
            key = random.randint(-1000, 1000)
            root.add(Node(key=key))
            array += [key]

        node0 = findfirstk_iterative(root, key)
        if node0.key != key or (node0.left and node0.left.key >= key):
            print "iterative failed."

        node1 = findfirstk_recursive(root, key)
        if node1.key != key or (node1.left and node1.left.key >= key):
            print "Recursive failed."

        node2 = findlargerthank(root, key)
        array.sort(reverse=True)
        index = array.index(key)
        if index:
            confkey = array[index - 1]
        else:
            confkey = None
        if not node2:
            if confkey:
                print "find larger failed."
        else:
            if node2.key != confkey:
                print "find larger failed."

    theset = set(xrange(-1000, 1000))
    for ind in xrange(testsize):
        # TESTS WHEN KEY IS NOT IN THE TREE.
        array = []
        root = Node()

        for x in xrange(size):
            key = random.randint(-1000, 1000)
            root.add(Node(key=key))
            array += [key]

        currentset = theset - set(array)
        key = currentset.pop()

        node0 = findfirstk_iterative(root, key)
        if node0:
            print node0.key,
            print "iterative failed."

        node1 = findfirstk_recursive(root, key)
        if node1:
            print node1.key,
            print "Recursive failed."

        key = max(array)
        node2 = findlargerthank(root, key)
        if node2:
            print node2.key,
            print "find larger failed."
