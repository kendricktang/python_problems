def findklargestelements(node, k):
    """Finds and returns k largest elements of the tree rooted at node.
    If there are less than k elements, then all the keys are returned."""
    if not node:
        return [], k

    # look for k largest elements in right child.
    largestelements, k = findklargestelements(node.right, k)
    if not k:
        return largestelements, 0

    # There remains k elements to be gathered.
    largestelements += [node.key]
    k -= 1

    # Check left child if there are still elements to be gathered!
    if k:
        rightlargestelements, k = findklargestelements(node.left, k)
        return largestelements + rightlargestelements, k

    return largestelements, k


if __name__ == "__main__":
    from node import Node
    from numpy import random

    size = 100
    random.seed(0)
    testsize = 100
    for ind in xrange(testsize):
        root = Node()
        array = []
        for x in xrange(size):
            key = random.randint(-1000, 1000)
            root.add(Node(key=key))
            array += [key]

        k = 11
        myresults = findklargestelements(root, k)[0]
        array.sort(reverse=True)
        if myresults != array[:k]:
            print "FAIL."
