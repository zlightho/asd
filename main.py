import unittest


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        if self.head is None:
            return

        prev_node = None
        node = self.head
        while node is not None:
            if node.value == val:
                if prev_node is None:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                if node == self.tail:
                    self.tail = prev_node
                if not all:
                    return
            else:
                prev_node = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is None:
            self.add_in_tail(newNode)
            return

        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return

        node = self.head
        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                if node == self.tail:
                    self.tail = newNode
                return
            node = node.next


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
        self.assertEqual(ll.len(), 3)

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

    def test_find_all():
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(3))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(4))
        linked_list.add_in_tail(Node(2))
        assert linked_list.find_all(2) == [
            linked_list.head.next.next,
            linked_list.head.next.next.next.next,
            linked_list.head.next.next.next.next.next,
        ]

        linked_list = LinkedList()
        assert linked_list.find_all(5) == []

    def test_len():
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

    def test_insert():
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

        linked_list.insert(linked_list.head.next.next.next, Node(7))
        assert linked_list.tail.value == 7


def sum_linked_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    result_list = LinkedList()

    if list1.len() != list2.len():
        return result_list

    node1 = list1.head
    node2 = list2.head
    while node1 is not None:
        sum_value = node1.value + node2.value
        new_node = Node(sum_value)
        result_list.add_in_tail(new_node)
        node1 = node1.next
        node2 = node2.next

    return result_list


def test_sum_linked_lists():
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
