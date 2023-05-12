from linkedlist2 import LinkedList2, Node

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        '''O(1), так как не нужно искать элементы или перестраивать структуру данных'''
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return None # если стек пустой

    def push(self, value):
        '''O(1), так как не нужно искать элементы или перестраивать структуру данных'''
        self.stack.append(value)
        
    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None # если стек пустой
        
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


def is_balanced(s: str) -> bool:
    stack = Stack() # создаем пустой стек

    # итерируемся по символам в строке s
    for char in s:
        if char == '(':
            stack.push('(')
        elif char == ')' and stack and stack.peek == '(':  
            stack.pop()  
        else:  
            return False

    return not stack