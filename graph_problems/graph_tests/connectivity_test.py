import unittest
from graph_algs.undirectedgraph import UndirectedGraph as UG


class TestFindExtendedContacts(unittest.TestCase):
    """A test suite for UndirectedGraph.checkconnectivity_*()
    (both 2E and 2A)."""

    def test_trivial_pass_zero(self):
        """Graphs with zero nodes are automatically very connected."""
        g = UG()
        self.assertTrue(g.checkconnectivity_2A())
        self.assertTrue(g.checkconnectivity_2E())

    def test_trivial_pass_one(self):
        """Graphs with one node are automatically very connected."""
        g = UG()
        g.addnode(42)
        self.assertTrue(g.checkconnectivity_2A())
        self.assertTrue(g.checkconnectivity_2E())

    def test_trivial_fail(self):
        """With just two nodes and one path, this isn't very connected."""
        g = UG()
        g.addpath(0, 1)
        self.assertFalse(g.checkconnectivity_2A())
        self.assertFalse(g.checkconnectivity_2E())

    def test_simple_pass(self):
        """Cyclic graphs are connected 2A and 2E."""
        g = UG()
        g.addpath(0, 1)
        g.addpath(1, 2)
        g.addpath(2, 0)
        self.assertTrue(g.checkconnectivity_2A())
        self.assertTrue(g.checkconnectivity_2E())

    def test_simple_fail(self):
        """A cycle makes a graph 2E, but not necessarily 2A."""
        g = UG()
        g.addpath(0, 1)
        g.addpath(1, 2)
        g.addpath(2, 0)
        g.addpath(3, 0)
        self.assertFalse(g.checkconnectivity_2A())
        self.assertTrue(g.checkconnectivity_2E())

    def test_textbook_fail(self):
        """Textbook example modified to be not 2E or 2A connected."""
        g = UG()
        g.addpath('a', 'b')
        g.addpath('b', 'e')
        g.addpath('e', 'd')
        g.addpath('d', 'c')
        g.addpath('e', 'f')
        g.addpath('e', 'h')
        g.addpath('f', 'g')
        g.addpath('f', 'i')
        g.addpath('i', 'j')
        g.addpath('i', 'm')
        g.addpath('m', 'k')
        g.addpath('k', 'l')
        self.assertFalse(g.checkconnectivity_2A())  # False
        self.assertFalse(g.checkconnectivity_2E())  # False

    def test_textbook_pass2E(self):
        """Textbook example of 2E connectedness."""
        g = UG()
        g.addpath('a', 'b')
        g.addpath('b', 'e')
        g.addpath('e', 'd')
        g.addpath('d', 'c')
        g.addpath('e', 'f')
        g.addpath('e', 'h')
        g.addpath('f', 'g')
        g.addpath('f', 'i')
        g.addpath('i', 'j')
        g.addpath('i', 'm')
        g.addpath('m', 'k')
        g.addpath('k', 'l')
        g.addpath('g', 'h')
        self.assertFalse(g.checkconnectivity_2A())  # False
        self.assertTrue(g.checkconnectivity_2E())  # True

    def test_textbook_passboth(self):
        """Textbook example of 2A connectedness."""
        g = UG()
        g.addpath('a', 'b')
        g.addpath('b', 'e')
        g.addpath('e', 'd')
        g.addpath('d', 'c')
        g.addpath('e', 'f')
        g.addpath('e', 'h')
        g.addpath('f', 'g')
        g.addpath('f', 'i')
        g.addpath('i', 'j')
        g.addpath('i', 'm')
        g.addpath('m', 'k')
        g.addpath('k', 'l')
        g.addpath('g', 'h')
        g.addpath('h', 'i')
        g.addpath('a', 'c')
        g.addpath('i', 'l')
        g.addpath('j', 'k')
        g.addpath('b', 'd')
        self.assertTrue(g.checkconnectivity_2A())  # True
        self.assertTrue(g.checkconnectivity_2E())  # True


if __name__ == "__main__":
    unittest.main()
