import unittest
from numpy import random as rand
from search_algs.twoarraysearch import findkthsmallest as fks


class TestFindKthSmallest(unittest.TestCase):
    """A test suite for findkthsmallest(),
    where inputs are two sorted arrays."""

    def test_singleelement(self):
        array = [42]
        k = 1
        val = fks(array, array, k)
        array.sort(reverse=True)
        self.assertEqual(val, 42)

    def test_onearraysmall(self):
        array0 = [-420]
        array1 = [-100, -50, -1, 0, 1, 50, 100]
        val = fks(array0, array1, 1)
        self.assertEqual(val, -420)

    def test_onearraybig(self):
        array0 = [420]
        array1 = [-100, -50, -1, 0, 1, 50, 100]
        val = fks(array0, array1, 8)
        self.assertEqual(val, 420)

    def test_bigtest(self):
        rand.seed(0)
        testsize = 1
        for ind in xrange(testsize):
            size0 = rand.randint(1, 20000)
            size1 = rand.randint(1, 20000)
            array0 = rand.randint(-100, 100, size0).tolist()
            array0.sort()
            array1 = rand.randint(-100, 100, size1).tolist()
            array1.sort()
            k = rand.randint(1, size0 + size1)
            val = fks(array0, array1, k)
            array2 = array0 + array1
            array2.sort()
            self.assertEqual(val, array2[k-1])


if __name__ == "__main__":
    unittest.main()
