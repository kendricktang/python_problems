def findk(root, k):
    """Root is a min-first BST, i.e. root.val is less than all keys,
    and all keys in the left tree are less than all keys in the right tree.

    Returns True if k is in the tree."""
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


if __name__ == "__main__":
    # Textbook example:
    from node import Node
    i = Node(key=23)
    h = Node(key=19, left=i)
    g = Node(key=17)
    c = Node(key=13, left=g, right=h)


    e = Node(key=7)
    f = Node(key=11)
    d = Node(key=5, left=e, right=f)
    b = Node(key=3, right=d)

    a = Node(key=2, left=b, right=c)

    if not findk(a, 5):
        print "Fail"
    if findk(a, 15):
        print "Fail"
