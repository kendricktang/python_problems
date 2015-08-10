import unittest
from bintree_algs.binarytree2 import BinaryTreeNode2 as BTN
from bintree_algs.makebintree import makefromstring as mfs
from bintree_algs.lowestcommonancestor import lca3 as lca


class TestLCA(unittest.TestCase):
    """Test suite for lowestcommonancestor.lca()."""

    def test_singlecase(self):
        """Test a tree with just a root."""
        s = "42"
        root = mfs(s, BTN)
        n1 = root.findnode(42)
        n2 = root.findnode(42)
        self.assertEqual(lca(n1, n2).val, 42)

    def test_node1isLCA(self):
        """Tests when node1 is the LCA of node1 and node2."""
        s = (
            "1(10(11(12(20(21(22[23(24)[25]]))[200]))" +
            "[13(14[15[16(17(18)[19])]])]))" +
            "[2[3(33(34)[35])[4(5(6)[7[8(9)]])]]]"
        )
        root = mfs(s, BTN)
        n1 = root.findnode(13)
        n2 = root.findnode(18)
        self.assertEqual(lca(n1, n2).val, 13)

    def test_node2isLCA(self):
        """Tests when node2 is the LCA of node1 and node2."""
        s = (
            "1(10(11(12(20(21(22[23(24)[25]]))[200]))" +
            "[13(14[15[16(17(18)[19])]])]))" +
            "[2[3(33(34)[35])[4(5(6)[7[8(9)]])]]]"
        )
        root = mfs(s, BTN)
        n1 = root.findnode(24)
        n2 = root.findnode(20)
        self.assertEqual(lca(n1, n2).val, 20)

    def test_differentbranches(self):
        """Tests when node1 and node2 are are not their LCA."""
        s = (
            "1(10(11(12(20(21(22[23(24)[25]]))[200]))" +
            "[13(14[15[16(17(18)[19])]])]))" +
            "[2[3(33(34)[35])[4(5(6)[7[8(9)]])]]]"
        )
        root = mfs(s, BTN)
        n1 = root.findnode(34)
        n2 = root.findnode(9)
        self.assertEqual(lca(n1, n2).val, 3)

    def test_verydifferentbranches(self):
        """Tests when the LCA is the root."""
        s = (
            "1(10(11(12(20(21(22[23(24)[25]]))[200]))" +
            "[13(14[15[16(17(18)[19])]])]))" +
            "[2[3(33(34)[35])[4(5(6)[7[8(9)]])]]]"
        )
        root = mfs(s, BTN)
        n1 = root.findnode(34)
        n2 = root.findnode(20)
        self.assertEqual(lca(n1, n2).val, 1)

    def test_exceptionthrow(self):
        """Tests when the node1 and node2 are in different trees."""
        s = (
            "1(10(11(12(20(21(22[23(24)[25]]))[200]))" +
            "[13(14[15[16(17(18)[19])]])]))" +
            "[2[3(33(34)[35])[4(5(6)[7[8(9)]])]]]"
        )
        root = mfs(s, BTN)
        n1 = root.findnode(34)
        n2 = BTN(42)
        try:
            lca(n1, n2)
        except StandardError:
            pass

"""
This is what the test tree looks like:
                        1
                10              2
            11                         3
        12         13            33           4
      20         14            34  35       5
    21  200           15                  6    7
22                        16                   8
  23                   17                     9
24 25				18   19
"""
if __name__ == '__main__':
    unittest.main()
