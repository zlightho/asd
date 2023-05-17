class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        """O(1), так как не нужно искать элементы или перестраивать
        структуру данных"""
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return None  # если стек пустой

    def push(self, value):
        """O(1), так как не нужно искать элементы или перестраивать
        структуру данных"""
        self.stack.append(value)

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None  # если стек пустой
