import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from main_tasks.simple_graph import SimpleGraph


class TestSimpleGraph(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(5)

    def test_add_vertex(self):
        self.graph.AddVertex(1)
        self.assertIsNotNone(self.graph.vertex[0])
        self.assertEqual(self.graph.vertex[0].Value, 1)
        # Проверка, что связи с новой вершиной отсутствуют
        for i in range(5):
            self.assertFalse(self.graph.IsEdge(0, i))

    def test_add_edge(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        # Проверка, что до добавления связи между вершинами не было
        self.assertFalse(self.graph.IsEdge(0, 1))
        self.graph.AddEdge(0, 1)
        # Проверка, что после добавления связь появилась
        self.assertTrue(self.graph.IsEdge(0, 1))
        self.assertTrue(self.graph.IsEdge(1, 0))

    def test_remove_edge(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddEdge(0, 1)
        # Проверка, что до удаления связь между вершинами была
        self.assertTrue(self.graph.IsEdge(0, 1))
        self.graph.RemoveEdge(0, 1)
        # Проверка, что после удаления связь отсутствует
        self.assertFalse(self.graph.IsEdge(0, 1))
        self.assertFalse(self.graph.IsEdge(1, 0))

    def test_remove_vertex(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        # Проверка, что до удаления некоторые вершины имеют связи с удаляемой вершиной
        self.assertTrue(self.graph.IsEdge(0, 1))
        self.assertTrue(self.graph.IsEdge(0, 2))
        self.graph.RemoveVertex(0)
        # Проверка, что после удаления этих связей нету
        self.assertIsNone(self.graph.vertex[0])
        for i in range(5):
            self.assertFalse(self.graph.IsEdge(0, i))
            self.assertFalse(self.graph.IsEdge(i, 0))

    def test_dfs_path_exists(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 4)
        path = self.graph.DepthFirstSearch(0, 4)
        self.assertEqual([v.Value for v in path], [1, 2, 3, 4, 5])

    def test_dfs_no_path(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        path = self.graph.DepthFirstSearch(0, 4)
        self.assertEqual(path, [])

    def test_dfs_same_node(self):
        self.graph.AddVertex(1)
        path = self.graph.DepthFirstSearch(0, 0)
        self.assertEqual([v.Value for v in path], [1])

    def test_bfs_path_exists(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 4)
        path = self.graph.BreadthFirstSearch(0, 4)
        self.assertEqual([v.Value for v in path], [1, 2, 3, 4, 5])

    def test_bfs_no_path(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        path = self.graph.BreadthFirstSearch(0, 4)
        self.assertEqual(path, [])

    def test_bfs_same_node(self):
        self.graph.AddVertex(1)
        path = self.graph.BreadthFirstSearch(0, 0)
        self.assertEqual([v.Value for v in path], [1])

    def test_weak_vertices_no_triangle(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        weak_vertices = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [1, 2, 3])

    def test_weak_vertices_with_triangle(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 0)
        self.graph.AddEdge(3, 4)
        weak_vertices = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [4, 5])

    def test_weak_vertices_all_in_triangle(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 0)
        weak_vertices = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [])

    def test_weak_vertices_multiple_triangles(self):
        self.graph = SimpleGraph(7)
        self.graph.AddVertex(0)
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddVertex(3)
        self.graph.AddVertex(4)
        self.graph.AddVertex(5)
        self.graph.AddVertex(6)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 0)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(3, 4)
        self.graph.AddEdge(4, 1)
        weak_vertices = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [5, 6])


if __name__ == "__main__":
    unittest.main()
