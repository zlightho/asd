import unittest

from main import LinkedList2, Node


class LinkedList2Tests(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList2()

    def test_add_in_tail(self):
        self.ll.add_in_tail(Node(1))
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.head.value, 1)
        self.ll.add_in_tail(Node(2))
        self.assertEqual(self.ll.tail.value, 2)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.tail.prev.value, 1)

    def test_add_in_head(self):
        self.ll.add_in_head(Node(1))
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.tail.value, 1)
        self.ll.add_in_head(Node(2))
        self.assertEqual(self.ll.head.value, 2)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.head.next.value, 1)

    def test_find(self):
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(3))
        self.assertEqual(self.ll.find(1), self.ll.head)
        self.assertEqual(self.ll.find(2), self.ll.head.next)
        self.assertEqual(self.ll.find(3), self.ll.tail)
        self.assertIsNone(self.ll.find(4))

    def test_find_all(self):
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(3))
        self.ll.add_in_tail(Node(1))
        self.assertEqual(
            self.ll.find_all(1), [self.ll.head, self.ll.tail.prev]
        )
        self.assertEqual(self.ll.find_all(2), [self.ll.head.next])
        self.assertEqual(self.ll.find_all(4), [])

    def test_delete(self):
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(3))
        self.ll.delete(1)
        self.assertEqual(self.ll.head.value, 2)
        self.ll.delete(3)
        self.assertEqual(self.ll.tail.value, 2)
        self.ll.delete(2)
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)

    def test_clean(self):
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(2))
        self.ll.clean()
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)

    def test_len(self):
        self.assertEqual(self.ll.len(), 0)
        self.ll.add_in_tail(Node(1))
        self.assertEqual(self.ll.len(), 1)
        self.ll.add_in_tail(Node(2))
        self.assertEqual(self.ll.len(), 2)
        self.ll.delete(2)
        self.assertEqual(self.ll.len(), 1)
        self.ll.delete(1)
        self.assertEqual(self.ll.len(), 0)

    def test_insert(self):
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(3))
        self.ll.insert(self.ll.head.next, Node(2))
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.head.next.value, 2)
        self.assertEqual(self.ll.head.next.prev.value, 1)
        self.assertEqual(self.ll.head.next.next.value, 1)
        self.assertEqual(self.ll.head.next.next.next.value, 3)
        self.assertEqual(self.ll.tail.value, 3)
        self.assertEqual(self.ll.tail.prev.value, 1)
        self.assertEqual(self.ll.tail.prev.prev.value, 2)
        self.ll.insert(self.ll.tail, Node(4))
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.tail.value, 4)


if __name__ == "__main__":
    unittest.main()
