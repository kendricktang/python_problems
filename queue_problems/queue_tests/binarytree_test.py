import unittest
from queue_algs.binarytree import printbinarytree as pbt
from queue_algs.nodes import BinaryNode


class TestPrintBinaryTree(unittest.TestCase):
    """Test suite for printbinarytree."""

    def test_book_example(self):
        binarytree = makebinarytree()
        outputstr = pbt(binarytree)
        expectedstr = "314,6,6,271,561,2,271,28,0,3,1,28,17,401,257,641"
        self.assertEqual(outputstr, expectedstr)
        print outputstr


def makebinarytree():
    D = BinaryNode(28)
    E = BinaryNode(0)
    C = BinaryNode(271, left=D, right=E)

    H = BinaryNode(17)
    G = BinaryNode(3, left=H)
    F = BinaryNode(561, right=G)
    B = BinaryNode(6, left=C, right=F)

    M = BinaryNode(641)
    L = BinaryNode(401, right=M)

    N = BinaryNode(257)
    K = BinaryNode(1, left=L, right=N)
    J = BinaryNode(2, right=K)

    P = BinaryNode(28)
    O = BinaryNode(271, right=P)
    I = BinaryNode(6, left=J, right=O)

    A = BinaryNode(314, left=B, right=I)
    return A


if __name__ == '__main__':
    unittest.main()
