import unittest
from graph_algs.stringproduction import findproductionseq as fps


class TestFindExtendedContacts(unittest.TestCase):
    """A test suite for circuitboard.isdivisible()."""

    def test_nosequence(self):
        """Test that no sequence is found when it shouldn't be."""
        string_dict = [
            "apple", "banana", "corkscrew", "donut", "elephant"
        ]
        self.assertEqual(fps(string_dict, "apple", "donut"), -1)

    def test_trivialcase(self):
        """Find the trivial path from a word to itself."""
        string_dict = [
            "apple", "banana", "corkscrew", "donut", "elephant"
        ]
        self.assertTrue(
            confirmproductionseq(
                fps(string_dict, "apple", "apple"),
                "apple", "apple")
        )

    def test_multipathcase(self):
        """Find a single path, even though multiple paths exist."""
        string_dict = [
            "cat", "hat", "bat", "mat", "lat",
            "cut", "hut", "but", "mut", "lut",
            "cur", "hur", "bur", "mur", "lur",
            "zur"
        ]
        self.assertTrue(
            confirmproductionseq(
                fps(string_dict, "cat", "zur"),
                "cat", "zur")
        )

    def test_fail(self):
        """Test a not so trivial failure."""
        string_dict = [
            "cat", "hat", "bat", "mat", "lat",
            "cut", "hut", "but", "mut", "lut",
            "cur", "hur", "bur", "mur", "lur",
            "zur", "zoo", "too", "moo", "poo"
        ]
        self.assertEqual(fps(string_dict, "zur", "zoo"), -1)


def isoneletteraway(s, t):
    if len(s) is not len(t):
        return False
    diffcount = sum([s[i] != t[i] for i in xrange(len(s))])
    return diffcount == 1


def confirmproductionseq(productionseq, s, t):
    if s != productionseq[0] or t != productionseq[-1]:
        return False
    prev = s
    for string in productionseq[1:]:
        if not isoneletteraway(prev, string):
            return False
        prev = string
    return True


if __name__ == "__main__":
    unittest.main()
