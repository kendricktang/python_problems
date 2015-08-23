import unittest
from numpy import random as rand
from search_algs.unsorted_findkth import findkthlargest as fkl


class TestFindKthLargest(unittest.TestCase):
    """A test suite for findkthlargest()."""

    def test_singleelement(self):
        array = [42]
        k = 1
        val = fkl(array, k)
        array.sort(reverse=True)
        self.assertEqual(val, array[k-1])

    def test_allrepeatedvalue(self):
        array = [42, 42, 42, 42, 42]
        k = 5
        val = fkl(array, k)
        array.sort(reverse=True)
        self.assertEqual(val, array[k-1])

    def test_tworepeatedvalues(self):
        array = [42, 42, 42, 42, 42, 40, 40, 40, 40]
        k = 6
        val = fkl(array, k)
        array.sort(reverse=True)
        self.assertEqual(val, array[k-1])

    def test_bigtest(self):
        rand.seed(0)
        testsize = 1
        for x in xrange(testsize):
            size = rand.randint(1, 20000)
            array = rand.randint(-100, 100, size)
            array = array.tolist()
            k = rand.randint(1, size + 1)
            val = fkl(array, k)
            array.sort(reverse=True)
            self.assertEqual(val, array[k-1])


if __name__ == "__main__":
    unittest.main()
