def makebintree(s, BTN):
    """Converts string into binary tree.
    Hierarchy is determined by parens.
    e.g. 1(2(3)[4])[5[10]] has 1 at the root, and its children are 2 and 5,
    and 2's child is 3 and 4, and 5 only has a right child with value 10.
    """

    if not s:
        return TypeError("input string must not be empty")

    root = BTN()
    return _makebintree(root, s)


def _makebintree(node, s):
    """Recursive helper for makebintree.
    s must be of the format n(...)[...], or be empty."""

    children_ind = -1

    for ind in xrange(len(s)):
        if not s[ind].isdigit() and not s[ind] is '-':
            children_ind = ind
            break

    if children_ind is -1:
        # No children!
        node.val = int(s)
        return node

    node.val = int(s[:children_ind])

    ind_0 = -1
    ind_1 = -1
    leftcount = 0
    rightcount = 0
    for ind in xrange(children_ind, len(s)):
        c = s[ind]
        if c is '(' or c is '[':
            if ind_0 is -1:
                ind_0 = ind
            leftcount += 1
        elif c is ')' or c is ']':
            rightcount += 1
        if leftcount is rightcount:
            ind_1 = ind + 1
            break

    if s[ind_0] is '[':
        # There is no left child
        rightnode = node.setright(None)
        _makebintree(rightnode, s[ind_0+1:ind_1-1])
        return node

    leftnode = node.setleft(None)
    _makebintree(leftnode, s[ind_0+1:ind_1-1])
    if ind_1 < len(s):
        # There is a right child
        rightnode = node.setright(None)
        _makebintree(rightnode, s[ind_1+1:-1])
    return node
