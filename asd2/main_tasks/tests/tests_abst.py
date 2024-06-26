import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from main_tasks.abst import aBST


class TestaBST(unittest.TestCase):
    def setUp(self):
        self.tree = aBST(2)

    def test_AddKey(self):
        self.assertEqual(self.tree.AddKey(10), 0)
        self.assertEqual(self.tree.AddKey(5), 1)
        self.assertEqual(self.tree.AddKey(15), 2)
        self.assertEqual(self.tree.AddKey(3), 3)
        self.assertEqual(self.tree.AddKey(7), 4)
        self.assertEqual(self.tree.AddKey(12), 5)
        self.assertEqual(self.tree.AddKey(18), 6)
        self.assertEqual(self.tree.AddKey(20), -1)

    def test_FindKeyIndex(self):
        self.tree.AddKey(10)
        self.tree.AddKey(5)
        self.tree.AddKey(15)
        self.assertEqual(self.tree.FindKeyIndex(10), 0)
        self.assertEqual(self.tree.FindKeyIndex(5), 1)
        self.assertEqual(self.tree.FindKeyIndex(15), 2)
        self.assertEqual(self.tree.FindKeyIndex(20), -6)

    def test_TreeArray(self):
        self.tree.AddKey(10)
        self.tree.AddKey(5)
        self.tree.AddKey(15)
        self.tree.AddKey(3)
        self.tree.AddKey(7)
        self.tree.AddKey(12)
        self.tree.AddKey(18)
        expected_tree = [10, 5, 15, 3, 7, 12, 18]
        self.assertEqual(self.tree.Tree, expected_tree)


if __name__ == "__main__":
    unittest.main()
