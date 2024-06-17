import unittest
from deque import Deque

class TestDeque(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_addFront(self):
        self.deque.addFront(1)
        self.assertEqual(self.deque.size(), 1)

    def test_addTail(self):
        self.deque.addTail(1)
        self.assertEqual(self.deque.size(), 1)

    def test_removeFront(self):
        self.deque.addFront(1)
        self.assertEqual(self.deque.removeFront(), 1)
        self.assertEqual(self.deque.size(), 0)

    def test_removeFront_empty(self):
        self.assertIsNone(self.deque.removeFront())

    def test_removeTail(self):
        self.deque.addTail(1)
        self.assertEqual(self.deque.removeTail(), 1)
        self.assertEqual(self.deque.size(), 0)

    def test_removeTail_empty(self):
        self.assertIsNone(self.deque.removeTail())

    def test_size(self):
        self.assertEqual(self.deque.size(), 0)
        self.deque.addFront(1)
        self.assertEqual(self.deque.size(), 1)
        self.deque.addTail(2)
        self.assertEqual(self.deque.size(), 2)
        self.deque.removeFront()
        self.assertEqual(self.deque.size(), 1)
        self.deque.removeTail()
        self.assertEqual(self.deque.size(), 0)

if __name__ == "__main__":
    unittest.main()
