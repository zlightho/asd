from linkedlist2 import LinkedList2, Node


class HeadStack:
    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        return self.stack.len()

    def pop(self):
        '''O(1), т.к. мы работаем только с головой списка'''
        if self.stack.head is not None:
            node = self.stack.head
            self.stack.delete(node)
        else:
            return None  # если стек пустой

    def push(self, value):
        '''O(1), т.к. мы работаем только с головой списка'''
        node = Node(value)
        self.stack.add_in_head(node)

    def peek(self):
        if self.stack.head is not None:
            return self.stack.head.value
        else:
            return None  # если стек пустой
