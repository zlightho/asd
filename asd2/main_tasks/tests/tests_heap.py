import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from main_tasks.heap import Heap

class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()

    def test_make_heap(self):
        array = [4, 10, 3, 5, 1]
        self.heap.MakeHeap(array, 2)
        self.assertEqual(self.heap.HeapArray[:self.heap.size], [10, 5, 3, 4, 1])

    def test_get_max(self):
        array = [4, 10, 3, 5, 1]
        self.heap.MakeHeap(array, 2)
        self.assertEqual(self.heap.GetMax(), 10)
        self.assertEqual(self.heap.HeapArray[:self.heap.size], [5, 4, 3, 1])

    def test_add(self):
        array = [4, 10, 3, 5, 1]
        self.heap.MakeHeap(array, 2)
        self.assertTrue(self.heap.Add(6))
        self.assertEqual(self.heap.HeapArray[:self.heap.size], [10, 5, 6, 4, 1, 3])

    def test_add_full(self):
        array = [4, 10, 3, 5, 1]
        self.heap.MakeHeap(array, 2)
        self.assertTrue(self.heap.Add(6))
        self.assertTrue(self.heap.Add(7))
        self.assertFalse(self.heap.Add(8))

if __name__ == '__main__':
    unittest.main()