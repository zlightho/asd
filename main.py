class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None and node.next is None:
                    self.head = None
                    self.tail = None
                    break
                if node.prev is None:
                    self.head = node.next
                    self.head.prev = None
                else:
                    node.prev.next = node.next
                if node.next is None:
                    self.tail = node.prev
                    self.tail.next = None
                else:
                    node.next.prev = node.prev
                if not all:
                    break
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode is None and self.head is not None:
            newNode.next = self.head
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        elif afterNode == self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next = newNode
            newNode.next.prev = newNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.head.prev = None
