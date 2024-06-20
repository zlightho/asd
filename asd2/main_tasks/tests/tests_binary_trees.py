import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from main_tasks.binary_trees import BST, BSTFind, BSTNode


class TestBST(unittest.TestCase):

    def setUp(self):
        self.root = BSTNode(10, "root", None)
        self.tree = BST(self.root)

    def test_FindNodeByKey_absent_key(self):
        find_result = self.tree.FindNodeByKey(5)
        self.assertFalse(find_result.NodeHasKey)
        self.assertTrue(find_result.ToLeft)
        self.assertEqual(find_result.Node, self.root)

        find_result = self.tree.FindNodeByKey(15)
        self.assertFalse(find_result.NodeHasKey)
        self.assertFalse(find_result.ToLeft)
        self.assertEqual(find_result.Node, self.root)

    def test_FindNodeByKey_present_key(self):
        self.tree.AddKeyValue(5, "left")
        find_result = self.tree.FindNodeByKey(5)
        self.assertTrue(find_result.NodeHasKey)
        self.assertEqual(find_result.Node.NodeKey, 5)
        self.assertEqual(find_result.Node.NodeValue, "left")

    def test_AddKeyValue(self):
        self.assertFalse(self.tree.FindNodeByKey(5).NodeHasKey)
        self.assertTrue(self.tree.AddKeyValue(5, "left"))
        self.assertTrue(self.tree.FindNodeByKey(5).NodeHasKey)
        self.assertFalse(self.tree.AddKeyValue(5, "left"))  # key already exists

    def test_AddKeyValue_left_right(self):
        self.tree.AddKeyValue(5, "left")
        self.tree.AddKeyValue(15, "right")
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 5)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 15)

    def test_FinMinMax(self):
        self.tree.AddKeyValue(5, "left")
        self.tree.AddKeyValue(15, "right")
        self.tree.AddKeyValue(2, "left-left")
        self.tree.AddKeyValue(7, "left-right")
        self.tree.AddKeyValue(12, "right-left")
        self.tree.AddKeyValue(20, "right-right")

        min_node = self.tree.FinMinMax(self.tree.Root, False)
        self.assertEqual(min_node.NodeKey, 2)
        max_node = self.tree.FinMinMax(self.tree.Root, True)
        self.assertEqual(max_node.NodeKey, 20)

        min_node = self.tree.FinMinMax(self.tree.Root.LeftChild, False)
        self.assertEqual(min_node.NodeKey, 2)
        max_node = self.tree.FinMinMax(self.tree.Root.LeftChild, True)
        self.assertEqual(max_node.NodeKey, 7)

        min_node = self.tree.FinMinMax(self.tree.Root.RightChild, False)
        self.assertEqual(min_node.NodeKey, 12)
        max_node = self.tree.FinMinMax(self.tree.Root.RightChild, True)
        self.assertEqual(max_node.NodeKey, 20)

    def test_DeleteNodeByKey(self):
        self.tree.AddKeyValue(5, "left")
        self.tree.AddKeyValue(15, "right")
        self.tree.AddKeyValue(2, "left-left")
        self.tree.AddKeyValue(7, "left-right")
        self.tree.AddKeyValue(12, "right-left")
        self.tree.AddKeyValue(20, "right-right")

        self.assertTrue(self.tree.DeleteNodeByKey(5))
        self.assertFalse(self.tree.FindNodeByKey(5).NodeHasKey)

        self.assertTrue(self.tree.DeleteNodeByKey(15))
        self.assertFalse(self.tree.FindNodeByKey(15).NodeHasKey)

        self.assertTrue(self.tree.DeleteNodeByKey(10))  # delete root
        self.assertFalse(self.tree.FindNodeByKey(10).NodeHasKey)

    def test_Count(self):
        self.assertEqual(self.tree.Count(), 1)
        self.tree.AddKeyValue(5, "left")
        self.tree.AddKeyValue(15, "right")
        self.assertEqual(self.tree.Count(), 3)


if __name__ == "__main__":
    unittest.main()
