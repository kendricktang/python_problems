from binarytree2 import BinaryTreeNode2 as BST


def makebintree(preorder):
    """Makes a binary tree given an pre-order traversal which indicates the
    children of leaf nodes as None's."""
    nodestack = []
    preorder.reverse()
    for element in preorder:
        if element:
            node = BST(element)
            leftchild = nodestack.pop()
            if leftchild:
                node.left = leftchild
                leftchild.parent = node

            rightchild = nodestack.pop()
            if rightchild:
                node.right = rightchild
                rightchild.parent = node

            nodestack.append(node)
        else:
            nodestack.append(None)
    preorder.reverse()
    return nodestack.pop()
