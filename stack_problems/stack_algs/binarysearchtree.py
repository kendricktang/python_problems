from nodes import BinaryNode
from stack import Stack


class BinarySearchTree(object):
    """A Binary search tree: node.left < node <= node.right

    Only add methods are implemented. Does not implement has, or delete.
    """

    def __init__(self, val):
        """Initiate a BST with a single value"""
        self.top = BinaryNode(val)

    @classmethod
    def fromarray(cls, array):
        """Initiate a BST with an array"""
        bst = cls(array[0])
        for i in xrange(1, len(array)):
            bst.add(array[i])
        return bst

    def add(self, val):
        """Search the BST and add a node to the BST with val"""
        node = self.top
        while node.hasnext(val):
            node = node.getnext(val)
        node.setnext(val)

    @staticmethod
    def print_BST(binarynode):
        """Prints a subset of a BST without recursion.
        This function will print the value at node and the value at
        all of node's children in sorted order.
        """

        stack = Stack()
        curr = binarynode
        print "<",
        while not stack.isempty() or curr:
            if curr:
                stack.push(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                currval = curr.val
                curr = curr.right
                print str(currval),
                if not stack.isempty() or curr:
                    print ',',
        print ">"

    @staticmethod
    def print_BST_test(binarynode):
        """This should be identical to print_BST in every way
        except it adds the elements to a list and returns it
        """

        stack = Stack()
        curr = binarynode
        lst = []
        while not stack.isempty() or curr:
            if curr:
                stack.push(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                currval = curr.val
                curr = curr.right
                lst.append(currval)
        return lst


if __name__ == "__main__":
    array = [1, 2, 3, 1, 2, 3, 30]
    bst = BinarySearchTree.fromarray(array)
    x = BinarySearchTree.print_BST_test(bst.top)
    print x
