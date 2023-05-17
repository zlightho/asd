class Queue:
    def __init__(self):
        # инициализация хранилища данных
        self.items = []

    def enqueue(self, item):
        """Вставка в хвост. O(1), так как список поддерживает быструю операцию
        добавления элемента в конец."""
        self.items.append(item)

    def dequeue(self):
        """Удаление элемента из начала списка требует перенумерации
        всех оставшихся элементов, чтобы заполнить пустую позицию
        в начале списка. Поэтому операция dequeue() имеет сложность O(n),
        где n - количество элементов в очереди"""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


def rotate_queue(queue, N):
    if N < 0 or N > queue.size():
        raise ValueError("Invalid rotation value")

    if N == 0:
        return

    for _ in range(N):
        item = queue.dequeue()
        queue.enqueue(item)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

rotate_queue(queue, 2)

while queue.size() > 0:
    print(queue.dequeue())  # Output: 3 4 5 1 2
