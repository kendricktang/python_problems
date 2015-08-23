import unittest
from bintree_algs.binarytree3 import BinaryTreeNode3 as BTN
from bintree_algs.makebintree import makefromstring as mfs


class TestFindKUnbalancedDescendent(unittest.TestCase):
    """Test suite for BinaryTreeNode.findkunbalanceddescendent."""

    def test_singlecase(self):
        """Test a tree with just a root."""
        s = "42"
        root = mfs(s, BTN)
        root.fixsize()
        self.assertEqual(
            root.find_kth_node(1).val,
            42)
        try:
            root.find_kth_node(2)
        except IndexError:
            pass

    def test_rightonly(self):
        """Test a tree with only a right side."""
        s = "42[-100(12(10)[11(999)[17]])[32]]"
        root = mfs(s, BTN)
        root.fixsize()
        self.assertEqual(
            root.find_kth_node(1).val,
            42)
        self.assertEqual(
            root.find_kth_node(3).val,
            12)
        self.assertEqual(
            root.find_kth_node(5).val,
            11)
        self.assertEqual(
            root.find_kth_node(7).val,
            -100)

    def test_leftonly(self):
        """Test a tree with only a left side."""
        s = "42(-100(12(10)[11[17[112233]]])[23])"
        root = mfs(s, BTN)
        root.fixsize()
        self.assertEqual(
            root.find_kth_node(1).val,
            10)
        self.assertEqual(
            root.find_kth_node(3).val,
            11)
        self.assertEqual(
            root.find_kth_node(5).val,
            112233)
        self.assertEqual(
            root.find_kth_node(7).val,
            23)

    def test_strictrightonly(self):
        """Test a tree with only right children."""
        s = "1[2[3[4[5[6]]]]]"
        root = mfs(s, BTN)
        root.fixsize()
        self.assertEqual(
            root.find_kth_node(1).val,
            1)
        self.assertEqual(
            root.find_kth_node(3).val,
            3)
        self.assertEqual(
            root.find_kth_node(5).val,
            5)

    def test_strictleftonly(self):
        """Test a tree with only left children."""
        s = "1(2(3(4(5(6)))))"
        root = mfs(s, BTN)
        root.fixsize()
        self.assertEqual(
            root.find_kth_node(1).val,
            6)
        self.assertEqual(
            root.find_kth_node(3).val,
            4)
        self.assertEqual(
            root.find_kth_node(5).val,
            2)

    def test_bothchildren(self):
        """Test a tree which has both children."""
        s = "42(-100(12)[28])[100(2000(1)[2])[111]]"
        root = mfs(s, BTN)
        root.fixsize()
        self.assertEqual(
            root.find_kth_node(1).val,
            12)
        self.assertEqual(
            root.find_kth_node(3).val,
            28)
        self.assertEqual(
            root.find_kth_node(5).val,
            1)
        self.assertEqual(
            root.find_kth_node(7).val,
            2)
        self.assertEqual(
            root.find_kth_node(9).val,
            111)


if __name__ == '__main__':
    unittest.main()
