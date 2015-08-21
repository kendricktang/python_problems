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


if __name__ == "__main__":
    from node import Node
    from numpy import random as rand
    rand.seed(0)
    testsize = 100
    for ind in xrange(testsize):
        size = rand.randint(50)
        root = Node(key=rand.randint(-50, 50))
        for ind in xrange(size):
            root.add(Node(rand.randint(-10, 10)), parent=True)

        mykey = rand.randint(-50, 50)
        mynode = Node(key=mykey)
        root.add(mynode, parent=True)
        successor = findsuccessor(mynode)
        bst = root.inordertraversal()
        myind = bst.index(mynode.key)

        if successor:
            if successor.key != bst[myind + 1]:
                print "FAIL"

        else:
            if myind != len(bst) - 1:
                print "FAIL2"
