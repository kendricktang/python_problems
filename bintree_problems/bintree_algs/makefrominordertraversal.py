from stack_algs.stack import Stack
from binarytree2 import BinaryTreeNode2 as BST


def makebintree(inorder):
    """Makes a binary tree given an in-order traversal which indicates the
    children of leaf nodes as None's."""
    nodestack = Stack()
    inorder.reverse()
    for element in inorder:
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

            nodestack.push(node)
        else:
            nodestack.push(None)
    inorder.reverse()
    return nodestack.pop()
