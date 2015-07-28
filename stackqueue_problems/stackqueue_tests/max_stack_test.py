import unittest
from stackqueue_algs.max_stack import MaxStack as ms
from stackqueue_algs.max_stack import MaxStackAlt as msa

class TestMaxStack(unittest.TestCase):
    """Test suite for MaxStack"""

    def test_single_case(self):
        """Test an array with a single value"""
        stack = [100]
        maxstack = ms.fromarray(stack)
        self.assertEqual(maxstack.getmax(), 100)

    def test_descending_case(self):
        """Test an array with a descending values"""
        stack = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        maxstack = ms.fromarray(stack)
        self.assertEqual(maxstack.getmax(), 10)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.pop(), 2)
        self.assertEqual(maxstack.pop(), 3)
        self.assertEqual(maxstack.getmax(), 10)

    def test_ascending_case(self):
        """Test an array with ascending values"""
        stack = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        maxstack = ms.fromarray(stack)
        self.assertEqual(maxstack.getmax(), 9)
        self.assertEqual(maxstack.pop(), 9)
        self.assertEqual(maxstack.pop(), 8)
        self.assertEqual(maxstack.pop(), 7)
        self.assertEqual(maxstack.getmax(), 6)
    
    def test_pop(self):
        """Test the ability to maintain knowledge of the maximum"""
        stack = [1,20,1,1,30,30,1,1,100,1]
        maxstack = ms.fromarray(stack)
        self.assertEqual(maxstack.getmax(), 100)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 100)
        self.assertEqual(maxstack.pop(), 100)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 30)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 30)
        self.assertEqual(maxstack.getmax(), 20)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 20)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 20)
        self.assertEqual(maxstack.pop(), 20)
        self.assertEqual(maxstack.getmax(), 1)
        maxstack.push(30)
        self.assertEqual(maxstack.getmax(), 30)
        maxstack.push(30)
        self.assertEqual(maxstack.getmax(), 30)
        maxstack.push(3)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 3)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 30)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 30)
        self.assertEqual(maxstack.getmax(), 1)


class TestMaxStackAlt(unittest.TestCase):
    """Test suite for MaxStackAlt"""

    def test_single_case(self):
        """Test an array with a single value"""
        stack = [100]
        maxstack = msa.fromarray(stack)
        self.assertEqual(maxstack.getmax(), 100)

    def test_descending_case(self):
        """Test an array with a descending values"""
        stack = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        maxstack = msa.fromarray(stack)
        self.assertEqual(maxstack.getmax(), 10)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.pop(), 2)
        self.assertEqual(maxstack.pop(), 3)
        self.assertEqual(maxstack.getmax(), 10)

    def test_ascending_case(self):
        """Test an array with ascending values"""
        stack = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        maxstack = msa.fromarray(stack)
        self.assertEqual(maxstack.getmax(), 9)
        self.assertEqual(maxstack.pop(), 9)
        self.assertEqual(maxstack.pop(), 8)
        self.assertEqual(maxstack.pop(), 7)
        self.assertEqual(maxstack.getmax(), 6)
    
    def test_pop(self):
        """Test the ability to maintain knowledge of the maximum"""
        stack = [1,20,1,1,30,30,1,1,100,1]
        maxstack = msa.fromarray(stack)
        self.assertEqual(maxstack.getmax(), 100)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 100)
        self.assertEqual(maxstack.pop(), 100)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 30)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 30)
        self.assertEqual(maxstack.getmax(), 20)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 20)
        self.assertEqual(maxstack.pop(), 1)
        self.assertEqual(maxstack.getmax(), 20)
        self.assertEqual(maxstack.pop(), 20)
        self.assertEqual(maxstack.getmax(), 1)
        maxstack.push(30)
        self.assertEqual(maxstack.getmax(), 30)
        maxstack.push(30)
        self.assertEqual(maxstack.getmax(), 30)
        maxstack.push(3)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 3)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 30)
        self.assertEqual(maxstack.getmax(), 30)
        self.assertEqual(maxstack.pop(), 30)
        self.assertEqual(maxstack.getmax(), 1)


if __name__ == '__main__':
    unittest.main()
