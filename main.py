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
        prev_node = None
        node = self.head
        while node:
            if node.value == val:
                if prev_node is None:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                if node.next is None:
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
        while node:
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
        while node and node != afterNode:
            node = node.next

        if node is None:
            return

        newNode.next = node.next
        node.next = newNode
        if node == self.tail:
            self.tail = newNode


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
