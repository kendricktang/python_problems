import unittest
from stack_algs.queue import Queue as Q


class TestQueue(unittest.TestCase):
    """Test suite for Queue"""

    def test_queue(self):
        """Enqueue and dequeue test"""
        q = Q()
        q.enqueue(42)
        q.enqueue(-1)
        q.enqueue(100)
        q.enqueue(12)
        q.enqueue(28)
        q.enqueue(12345)
        self.assertEqual(q.dequeue(), 42)
        self.assertEqual(q.dequeue(), -1)
        self.assertEqual(q.dequeue(), 100)
        self.assertEqual(q.dequeue(), 12)
        self.assertEqual(q.dequeue(), 28)
        self.assertEqual(q.dequeue(), 12345)
        self.assertTrue(q.isempty())
        q.enqueue("yay")
        self.assertEqual(q.dequeue(), "yay")

    def test_max(self):
        """Tests getmax functionality"""
        q = Q()
        q.enqueue(42)
        q.enqueue(32)
        q.enqueue(-100)
        q.enqueue(41)

        self.assertEqual(q.getmax(), 42)
        q.dequeue()
        self.assertEqual(q.getmax(), 41)
        q.dequeue()
        self.assertEqual(q.getmax(), 41)
        q.dequeue()
        self.assertEqual(q.getmax(), 41)


if __name__ == '__main__':
    unittest.main()
