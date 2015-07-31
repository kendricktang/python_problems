import unittest
from stackqueue_algs.towersofhanoi import towersofhanoi as toh
from stackqueue_algs.towersofhanoi import TowerOfHanoi as TOH

class TestTowersOfHanoi(unittest.TestCase):
    """Test suite for TowersOfHanoi"""

    def test_3(self):
        """Test size 3 towers of hanoi"""
        size = 3
        targ, movecount = toh(size, suppress = True)
        self.assertEqual(
            [i for i in xrange(1,size+1)], 
            targ.toarray())
        self.assertEqual(2**size-1, movecount)

    def test_15(self):
        """Test size 15 towers of hanoi"""
        size = 15
        targ, movecount = toh(size, suppress = True)
        self.assertEqual(
            [i for i in xrange(1,size+1)], 
            targ.toarray())
        self.assertEqual(2**size-1, movecount)

if __name__ == '__main__':
    unittest.main()
