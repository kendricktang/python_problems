def makefromstring(s, BTN):
    """Converts string into binary tree.
    Hierarchy is determined by parens.
    e.g. 1(2(3)[4])[5[10]] has 1 at the root, and its children are 2 and 5,
    and 2's child is 3 and 4, and 5 only has a right child with value 10.
    """

    if not s:
        return TypeError("input string must not be empty")

    root = BTN()
    return _makefromstring(root, s)


def _makefromstring(node, s):
    """Recursive helper for makefromstring.
    s must be of the format n(...)[...], or be empty."""

    # Set node.val
    children_ind = _getindexofvalue(s)
    if children_ind is -1:
        # No children!
        node.val = int(s)
        return node

    node.val = int(s[:children_ind])

    ind_right = _getindicesofparens(s[children_ind:])
    try:
        ind_right += children_ind
    except TypeError:
        print s

    if s[children_ind] is '[':
        # There is no left child
        rightnode = node.setright(None)
        _makefromstring(rightnode, s[children_ind+1:ind_right-1])
        return node

    leftnode = node.setleft(None)
    _makefromstring(leftnode, s[children_ind+1:ind_right-1])
    if ind_right < len(s):
        # There is a right child
        rightnode = node.setright(None)
        _makefromstring(rightnode, s[ind_right+1:-1])
    return node


def _getindexofvalue(s):
    """Determines where the first '(' or '[' is in the string.
    If there are no parens, then this returns -1."""
    round_ind = s.find('(')
    square_ind = s.find('[')

    if round_ind is -1:
        return square_ind
    if square_ind is -1:
        return round_ind

    return min(round_ind, square_ind)


def _getindicesofparens(s):
    """Determines where the first set of outer parens is."""
    leftcount = 0
    rightcount = 0
    for ind in xrange(len(s)):
        c = s[ind]
        if c is '(' or c is '[':
            leftcount += 1
        elif c is ')' or c is ']':
            rightcount += 1
        if leftcount is rightcount:
            return ind + 1


def makefromtraversals(BTN, inorder, preorder=None, postorder=None):
    """Constructs a tree and returns the root if given an in-order traversal,
    and either a preorder or post order traversal."""
    root = BTN()
    if preorder:
        _makefrompretraversal(root, inorder, preorder)
        return root
    if postorder:
        _makefromposttraversal(root, inorder, postorder)
        return root
    raise TypeError("Preorder or postorder must be valid.")


def _makefrompretraversal(node, inorder, preorder):
    """Recursive helper for makefromtraversals() using pre-order traversal."""
    node.val = preorder[0]
    nodeindex = inorder.index(node.val)

    leftchild = inorder[:nodeindex]
    rightchild = inorder[nodeindex+1:]

    mysize = 1
    if leftchild:
        leftnode = node.setleft()
        mysize += _makefrompretraversal(
            leftnode, leftchild,
            preorder[1:])

    if rightchild:
        rightnode = node.setright()
        mysize += _makefrompretraversal(
            rightnode, rightchild,
            preorder[mysize:])
    return mysize


def _makefromposttraversal(node, inorder, postorder):
    """Recursive helper for makefromtraversals() using post-order traversal."""
    nodeval = postorder[-1]
    node.val = int(nodeval)
    nodeindex = inorder.index(nodeval)

    leftchild = inorder[:nodeindex]
    rightchild = inorder[nodeindex+1:]

    mysize = 1
    if rightchild:
        rightnode = node.setright()
        mysize += _makefromposttraversal(
            rightnode, rightchild,
            postorder[:-mysize])

    if leftchild:
        leftnode = node.setleft()
        mysize += _makefromposttraversal(
            leftnode, leftchild,
            postorder[:-mysize])

    return mysize
