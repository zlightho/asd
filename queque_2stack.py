from stack import Stack


class Queue:
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()

    def enqueue(self, item):
        self.input_stack.push(item)

    def dequeue(self):
        if self.output_stack.size() == 0:
            while self.input_stack.size() > 0:
                self.output_stack.push(self.input_stack.pop())

        if self.output_stack.size() > 0:
            return self.output_stack.pop()
        else:
            return None

    def size(self):
        return self.input_stack.size() + self.output_stack.size()


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

queue.enqueue(4)

print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: 4

print(queue.dequeue())  # Output: None (очередь пуста)
