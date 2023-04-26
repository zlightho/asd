import unittest

from main import Node, LinkedList, sum_linked_lists


class LinkedListTests(unittest.TestCase):
    def test_delete(self):
        ll = LinkedList()
        ll.add_in_tail(Node(10))
        ll.add_in_tail(Node(20))
        ll.add_in_tail(Node(30))
        ll.add_in_tail(Node(20))
        ll.add_in_tail(Node(40))

        ll.delete(20)

        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 40)
        self.assertEqual(ll.len(), 4)

    def test_delete_all(self):
        ll = LinkedList()
        ll.add_in_tail(Node(10))
        ll.add_in_tail(Node(20))
        ll.add_in_tail(Node(30))
        ll.add_in_tail(Node(20))
        ll.add_in_tail(Node(40))

        ll.delete(20, all=True)

        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 40)
        self.assertEqual(ll.len(), 3)

    def test_clean(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(3))

        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.head.next.value, 2)
        self.assertEqual(linked_list.head.next.next.value, 3)
        self.assertEqual(linked_list.tail.value, 3)
        self.assertEqual(linked_list.len(), 3)

        linked_list.clean()

        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertEqual(linked_list.len(), 0)

        linked_list.clean()
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertEqual(linked_list.len(), 0)

    def test_find_all(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(3))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(4))
        linked_list.add_in_tail(Node(2))
        assert linked_list.find_all(2) == [
            linked_list.head.next,
            linked_list.head.next.next.next,
            linked_list.head.next.next.next.next.next,
        ]

        linked_list = LinkedList()
        assert linked_list.find_all(5) == []

    def test_len(self):
        linked_list = LinkedList()
        assert linked_list.len() == 0

        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(3))
        assert linked_list.len() == 3

        linked_list.delete(1)
        linked_list.delete(3, True)
        assert linked_list.len() == 1

        linked_list.clean()
        assert linked_list.len() == 0

    def test_insert(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(3))
        linked_list.add_in_tail(Node(4))
        linked_list.insert(None, Node(5))
        assert linked_list.head.value == 5
        assert linked_list.head.next.value == 1

        linked_list.insert(linked_list.head.next, Node(6))
        assert linked_list.head.next.next.value == 6
        assert linked_list.head.next.next.next.value == 2


class SumLinkedListTests(unittest.TestCase):
    def test_sum_linked_lists(self):
        list1 = LinkedList()
        list2 = LinkedList()
        assert sum_linked_lists(list1, list2).len() == 0

        list1 = LinkedList()
        list1.add_in_tail(Node(1))
        list1.add_in_tail(Node(2))
        list1.add_in_tail(Node(3))

        list2 = LinkedList()
        list2.add_in_tail(Node(1))
        list2.add_in_tail(Node(2))

        assert sum_linked_lists(list1, list2).len() == 0

        list1 = LinkedList()
        list1.add_in_tail(Node(1))
        list1.add_in_tail(Node(2))
        list1.add_in_tail(Node(3))

        list2 = LinkedList()
        list2.add_in_tail(Node(1))
        list2.add_in_tail(Node(2))
        list2.add_in_tail(Node(3))

        result_list = sum_linked_lists(list1, list2)

        assert result_list.len() == 3
        assert result_list.head.value == 2
        assert result_list.head.next.value == 4
        assert result_list.tail.value == 6

        list1 = LinkedList()
        list1.add_in_tail(Node(1))
        list1.add_in_tail(Node(2))

        list2 = LinkedList()
        list2.add_in_tail(Node(3))
        list2.add_in_tail(Node(4))

        result_list = sum_linked_lists(list1, list2)

        assert result_list.len() == 2
        assert result_list.head.value == 4
        assert result_list.head.next.value == 6


if __name__ == "__main__":
    unittest.main()
