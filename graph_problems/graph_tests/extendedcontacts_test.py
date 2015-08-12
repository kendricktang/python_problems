import unittest
from graph_algs.graph import Graph


class TestFindExtendedContacts(unittest.TestCase):
    """A test suite for Graph.findallextendedcontacts()."""

    def test_singlecase(self):
        """Only one person in network."""
        g = Graph()
        g.addnode("z")
        extendedcontacts = g.findallextendedcontacts()
        self.assertEqual(extendedcontacts["z"], ["z"])

    def test_cycliccase(self):
        """Simple cyclic directional graph."""
        g = Graph()
        g.addpath("r", "s")
        g.addpath("s", "t")
        g.addpath("t", "r")
        extendedcontacts = g.findallextendedcontacts()
        self.assertEqual(set(extendedcontacts["r"]), set(["r", "s", "t"]))
        self.assertEqual(set(extendedcontacts["s"]), set(["s", "t", "r"]))
        self.assertEqual(set(extendedcontacts["t"]), set(["r", "s", "t"]))

    def test_disconnectedcase(self):
        """A graph made of two connected subgraphs."""
        g = Graph()
        g.addpath("a", "b")
        g.addpath("b", "e")
        g.addpath("e", "d")
        g.addpath("d", "c")
        g.addpath("e", "f")
        g.addpath("e", "h")
        g.addpath("g", "c")

        g.addpath("i", "j")
        g.addpath("i", "m")
        g.addpath("m", "k")
        g.addpath("k", "l")
        extendedcontacts = g.findallextendedcontacts()
        self.assertEqual(
            set(extendedcontacts["a"]),
            set(["a", "b", "d", "c", "e", "f", "h", "f"]))
        self.assertEqual(
            set(extendedcontacts["g"]),
            set(["g", "c"]))
        self.assertEqual(
            set(extendedcontacts["i"]),
            set(["i", "j", "m", "k", "l"]))
        self.assertEqual(
            set(extendedcontacts["m"]),
            set(["m", "k", "l"]))


if __name__ == "__main__":
    unittest.main()
