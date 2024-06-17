import unittest

from linkedlist2 import LinkedList2, Node


class LinkedList2Tests(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList2()

    def test_add_in_tail(self):
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.head.value, 1)
        ll.add_in_tail(Node(2))
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.prev.value, 1)

    def test_add_in_head(self):
        ll = LinkedList2()
        ll.add_in_head(Node(1))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 1)
        ll.add_in_head(Node(2))
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.head.next.value, 1)

    def test_find(self):
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        self.assertEqual(ll.find(1), ll.head)
        self.assertEqual(ll.find(2), ll.head.next)
        self.assertEqual(ll.find(3), ll.tail)
        self.assertIsNone(ll.find(4))

    def test_find_all(self):
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.add_in_tail(Node(1))
        self.assertEqual(ll.find_all(1), [ll.head, ll.tail.prev])
        self.assertEqual(ll.find_all(2), [ll.head.next])
        self.assertEqual(ll.find_all(4), [])

    def test_delete(self):
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(1)
        self.assertEqual(ll.head.value, 2)
        ll.delete(3)
        self.assertEqual(ll.tail.value, 2)
        ll.delete(2)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_clean(self):
        ll = LinkedList2()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.clean()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_len(self):
        ll = LinkedList2()
        self.assertEqual(ll.len(), 0)
        ll.add_in_tail(Node(1))
        self.assertEqual(ll.len(), 1)
        ll.add_in_tail(Node(2))
        self.assertEqual(ll.len(), 2)
        ll.delete(2)
        self.assertEqual(ll.len(), 1)
        ll.delete(1)
        self.assertEqual(ll.len(), 0)

    def test_insert(self):
        ll = LinkedList2()
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(1))
        self.ll.add_in_tail(Node(2))
        self.ll.add_in_tail(Node(3))
        self.ll.insert(ll.head.next, Node(2))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.head.next.value, 2)
        self.assertEqual(ll.head.next.prev.value, 1)
        self.assertEqual(ll.head.next.next.value, 1)
        self.assertEqual(ll.head.next.next.next.value, 3)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.tail.prev.value, 1)
        self.assertEqual(ll.tail.prev.prev.value, 2)
        self.ll.insert(ll.tail, Node(4))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 4)


if __name__ == "__main__":
    unittest.main()
