import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from main_tasks.simple_trees import (
    SimpleTree,
    SimpleTreeNode,
)


class TestSimpleTree(unittest.TestCase):

    def setUp(self):
        self.root = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.root)

    def test_AddChild(self):
        child = SimpleTreeNode(2, None)
        self.tree.AddChild(self.root, child)
        self.assertIn(child, self.root.Children)
        self.assertEqual(child.Parent, self.root)

    def test_DeleteNode(self):
        child = SimpleTreeNode(2, None)
        self.tree.AddChild(self.root, child)
        self.tree.DeleteNode(child)
        self.assertNotIn(child, self.root.Children)
        self.assertIsNone(child.Parent)

    def test_DeleteSubtree(self):
        child1 = SimpleTreeNode(2, None)
        child2 = SimpleTreeNode(3, None)
        grandchild = SimpleTreeNode(4, None)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(child1, grandchild)
        self.tree.AddChild(self.root, child2)

        self.tree.DeleteNode(child1)
        all_nodes = self.tree.GetAllNodes()

        self.assertNotIn(child1, all_nodes)
        self.assertNotIn(grandchild, all_nodes)

    def test_GetAllNodes(self):
        child1 = SimpleTreeNode(2, None)
        child2 = SimpleTreeNode(3, None)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(len(all_nodes), 3)  # root, child1, child2
        self.assertIn(self.root, all_nodes)
        self.assertIn(child1, all_nodes)
        self.assertIn(child2, all_nodes)

    def test_FindNodesByValue(self):
        child1 = SimpleTreeNode(2, None)
        child2 = SimpleTreeNode(2, None)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        found_nodes = self.tree.FindNodesByValue(2)
        self.assertEqual(len(found_nodes), 2)
        self.assertIn(child1, found_nodes)
        self.assertIn(child2, found_nodes)

    def test_MoveNode(self):
        child1 = SimpleTreeNode(2, None)
        child2 = SimpleTreeNode(3, None)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        self.tree.MoveNode(child1, child2)
        self.assertNotIn(child1, self.root.Children)
        self.assertIn(child1, child2.Children)
        self.assertEqual(child1.Parent, child2)

    def test_Count(self):
        child1 = SimpleTreeNode(2, None)
        child2 = SimpleTreeNode(3, None)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        self.assertEqual(self.tree.Count(), 3)  # root, child1, child2

    def test_LeafCount(self):
        child1 = SimpleTreeNode(2, None)
        child2 = SimpleTreeNode(3, None)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        self.assertEqual(self.tree.LeafCount(), 2)  # child1, child2


if __name__ == "__main__":
    unittest.main()
