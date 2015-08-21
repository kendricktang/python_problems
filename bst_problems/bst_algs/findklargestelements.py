def findklargestelements(node, k):
    return _findklargestelements(node, k)[0]

def _findklargestelements(node, k):
    """Finds and returns k largest elements of the tree rooted at node.
    If there are less than k elements, then all the keys are returned."""
    if not node:
        return [], k

    # look for k largest elements in right child.
    largestelements, k = _findklargestelements(node.right, k)
    if not k:
        return largestelements, 0

    # There remains k elements to be gathered.
    largestelements += [node.key]
    k -= 1

    # Check left child if there are still elements to be gathered!
    if k:
        rightlargestelements, k = _findklargestelements(node.left, k)
        return largestelements + rightlargestelements, k

    return largestelements, k
