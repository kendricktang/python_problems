import unittest
from numpy import random as rand
from search_algs.unsorted_findminmax import findminmax as fmm


class TestFindMinMax(unittest.TestCase):
    """A test suite for findminmax()."""

    def test_singleelement(self):
        array = [42]
        (_min, _max) = fmm(array)
        self.assertEqual(_min, min(array))
        self.assertEqual(_max, max(array))

    def test_allrepeatedvalue(self):
        array = [42, 42, 42, 42, 42]
        (_min, _max) = fmm(array)
        self.assertEqual(_min, min(array))
        self.assertEqual(_max, max(array))

    def test_tworepeatedvalues(self):
        array = [42, 42, 42, 42, 42, 40, 40, 40, 40]
        (_min, _max) = fmm(array)
        self.assertEqual(_min, min(array))
        self.assertEqual(_max, max(array))

    def test_bigtest(self):
        rand.seed(0)
        testsize = 1
        for ind in xrange(testsize):
            size = rand.randint(1, 20000)
            array = rand.randint(-100, 100, size)
            array = array.tolist()
            (_min, _max) = fmm(array)
            self.assertEqual(_min, min(array))
            self.assertEqual(_max, max(array))


if __name__ == "__main__":
    unittest.main()
