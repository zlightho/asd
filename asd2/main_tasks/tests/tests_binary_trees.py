import sys
import os
import unittest
from main_tasks.binary_trees import BST, BSTNode, BalancedBST

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


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
        self.assertFalse(self.tree.AddKeyValue(5, "left"))

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

        self.assertTrue(self.tree.DeleteNodeByKey(10))
        self.assertFalse(self.tree.FindNodeByKey(10).NodeHasKey)

    def test_Count(self):
        self.assertEqual(self.tree.Count(), 1)
        self.tree.AddKeyValue(5, "left")
        self.tree.AddKeyValue(15, "right")
        self.assertEqual(self.tree.Count(), 3)

    def test_WideAllNodes(self):
        self.tree.AddKeyValue(5, "left")
        self.tree.AddKeyValue(15, "right")
        self.tree.AddKeyValue(2, "left-left")
        self.tree.AddKeyValue(7, "left-right")
        self.tree.AddKeyValue(12, "right-left")
        self.tree.AddKeyValue(20, "right-right")

        wide_all_nodes = self.tree.WideAllNodes()
        expected_keys = [10, 5, 15, 2, 7, 12, 20]
        self.assertEqual([node.NodeKey for node in wide_all_nodes], expected_keys)

    def test_DeepAllNodes_in_order(self):
        self.tree.AddKeyValue(5, "left")
        self.tree.AddKeyValue(15, "right")
        self.tree.AddKeyValue(2, "left-left")
        self.tree.AddKeyValue(7, "left-right")
        self.tree.AddKeyValue(12, "right-left")
        self.tree.AddKeyValue(20, "right-right")

        deep_all_nodes = self.tree.DeepAllNodes(0)
        expected_keys = [2, 5, 7, 10, 12, 15, 20]
        self.assertEqual([node.NodeKey for node in deep_all_nodes], expected_keys)

    def test_DeepAllNodes_post_order(self):
        self.tree.AddKeyValue(5, "left")
        self.tree.AddKeyValue(15, "right")
        self.tree.AddKeyValue(2, "left-left")
        self.tree.AddKeyValue(7, "left-right")
        self.tree.AddKeyValue(12, "right-left")
        self.tree.AddKeyValue(20, "right-right")

        deep_all_nodes = self.tree.DeepAllNodes(1)
        expected_keys = [2, 7, 5, 12, 20, 15, 10]
        self.assertEqual([node.NodeKey for node in deep_all_nodes], expected_keys)

    def test_DeepAllNodes_pre_order(self):
        self.tree.AddKeyValue(5, "left")
        self.tree.AddKeyValue(15, "right")
        self.tree.AddKeyValue(2, "left-left")
        self.tree.AddKeyValue(7, "left-right")
        self.tree.AddKeyValue(12, "right-left")
        self.tree.AddKeyValue(20, "right-right")

        deep_all_nodes = self.tree.DeepAllNodes(2)
        expected_keys = [10, 5, 2, 7, 15, 12, 20]
        self.assertEqual([node.NodeKey for node in deep_all_nodes], expected_keys)


class TestBalancedBST(unittest.TestCase):
    def setUp(self):
        self.bst = BalancedBST()

    def test_generate_tree(self):
        self.bst.GenerateTree([1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

    def test_generate_tree_single_element(self):
        self.bst.GenerateTree([1])
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

    def test_generate_tree_two_elements(self):
        self.bst.GenerateTree([1, 2])
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

    def test_generate_tree_unbalanced(self):
        self.bst.GenerateTree([1, 2, 3, 4, 5])
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

    def test_is_balanced_empty_tree(self):
        self.assertTrue(self.bst.IsBalanced(None))


if __name__ == "__main__":
    unittest.main()
