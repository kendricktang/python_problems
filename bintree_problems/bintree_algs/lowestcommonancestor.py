def lca(root, node1, node2):
    """Returns the lowest common ancestors of node1 and node2 where the tree
    is made of binary tree nodes without parent pointers. Runs in O(n) time."""
    if node1 is node2:
        return node1

    return _lca(root, node1, node2)


def _lca(curr, node1, node2):
    """Recursive helper for lca()."""
    if not curr:
        # Walked off of a leaf node! Did not find anything.
        return None

    if node1 is curr or node2 is curr:
        # If one of the nodes is found, stop recursion. Suppose node1 is found.
        # then there are two cases: node2 is a descendent of node1, or node2 is
        # in a different branch. Both cases are covered here.
        return curr

    left_res = _lca(curr.left, node1, node2)
    right_res = _lca(curr.right, node1, node2)

    if left_res and right_res:
        # node1 and node2 are in two different branches, which means curr is
        # the LCA. Return curr.
        return curr

    # Returns either a found node, or None.
    if left_res:
        return left_res
    return right_res


def lca2(root, node1, node2):
    """A LCA algorithm using parent pointers in O(h) time and O(1) space."""
    node1height = findheight(root, node1)
    node2height = findheight(root, node2)

    # Swap so that node1 is lower down the tree than node 2.
    if node1height < node2height:
        node1, node2 = node2, node1
        node1height, node2height = node2height, node1height

    # Bring node1 to the same height as node2
    while node1height > node2height:
        node1 = node1.parent
        node1height -= 1

    # Bring them both up until they are equal.
    while node1 is not node2:
        node1 = node1.parent
        node2 = node2.parent

    return node1


def findheight(root, node):
    nodeheight = 0
    nodetemp = node
    while nodetemp is not root:
        nodetemp = nodetemp.parent
        nodeheight += 1
    return nodeheight


def lca3(node1, node2):
    """An LCA algorithm which runs in
    O(max(depth(node1)-depth(LCA),depth(node2)-depth(LCA)))"""
    parentset = set()
    while node1 or node2:
        if node1:
            if node1 in parentset:
                return node1
            else:
                parentset.add(node1)
                node1 = node1.parent

        if node2:
            if node2 in parentset:
                return node2
            else:
                parentset.add(node2)
                node2 = node2.parent

    raise StandardError(
        "Node1 and Node2 have no LCA. They are from different trees")
