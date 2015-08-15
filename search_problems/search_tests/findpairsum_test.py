import unittest
from numpy import random as rand
from search_algs.absarraysearch import findpairsum as fps


class TestFindPairSum(unittest.TestCase):
    """A test suite for findpairsum(). The input is an array
    sorted by absolute value."""

    def test_trivialcase_pass(self):
        array = [-10, 10]
        k = 0
        self.assertEqual([0, 1], fps(array, k))

    def test_trivialcase_fail(self):
        array = [-10, 10]
        k = 10
        self.assertEqual([-1, -1], fps(array, k))

    def test_textbookcase_pass(self):
        array = [-49, 75, 103, -147, 164, -197, -238, 314, 348, -422]
        k = 167
        self.assertEqual([3, 7], fps(array, k))

    def test_textbookcase_fail(self):
        array = [-49, 75, 103, -147, 164, -197, -238, 314, 348, -422]
        k = 0
        self.assertEqual([-1, -1], fps(array, k))

    def test_bigtest(self):
        """This only checks if (-1, -1) is not returned..."""
        rand.seed(1)
        testsize = 1
        for ind in xrange(testsize):
            size = rand.randint(1, 2000)
            array = rand.randint(-100, 100, size)
            array = sorted(array, key=lambda x: abs(x))
            k = rand.randint(-500, 500)
            ind0, ind1 = fps(array, k)
            if ind0 != -1:
                self.assertEqual(k, array[ind0] + array[ind1])


if __name__ == "__main__":
    unittest.main()
