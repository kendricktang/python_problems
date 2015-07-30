import unittest
from stackqueue_algs.towersofhanoi import towersofhanoi as toh
from stackqueue_algs.towersofhanoi import TowerOfHanoi as TOH

class TestTowersOfHanoi(unittest.TestCase):
    """Test suite for TowersOfHanoi"""

    def test_3(self):
        """Test size 3 towers of hanoi"""
        size = 3
        self.assertEqual(
            [i for i in xrange(1,size+1)], 
            toh(size, suppress = True).toarray())

    def test_15(self):
        size = 15
        """Test size 15 towers of hanoi"""
        self.assertEqual(
            [i for i in xrange(1,size+1)],
            toh(size, suppress = True).toarray())

if __name__ == '__main__':
    unittest.main()
