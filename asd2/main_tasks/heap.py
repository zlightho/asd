class Heap:
    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.size = 0  # текущее количество элементов в куче

    def MakeHeap(self, a, depth):
        max_size = 2 ** (depth + 1) - 1  # Максимальный размер кучи для заданной глубины
        self.HeapArray = [None] * max_size
        self.size = 0
        for key in a:
            self.Add(key)

    def GetMax(self):
        if self.size == 0:
            return -1  # если куча пуста
        max_elem = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.size - 1]
        self.HeapArray[self.size - 1] = None
        self.size -= 1
        self._sift_down(0)
        return max_elem

    def Add(self, key):
        if self.size == len(self.HeapArray):
            return False  # если куча вся заполнена
        self.HeapArray[self.size] = key
        self._sift_up(self.size)
        self.size += 1
        return True

    def _sift_down(self, idx):
        max_idx = idx
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2

        if left_child < self.size and self.HeapArray[left_child] > self.HeapArray[max_idx]:
            max_idx = left_child
        if right_child < self.size and self.HeapArray[right_child] > self.HeapArray[max_idx]:
            max_idx = right_child

        if max_idx != idx:
            self.HeapArray[idx], self.HeapArray[max_idx] = self.HeapArray[max_idx], self.HeapArray[idx]
            self._sift_down(max_idx)

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.HeapArray[idx] > self.HeapArray[parent]:
            self.HeapArray[idx], self.HeapArray[parent] = self.HeapArray[parent], self.HeapArray[idx]
            self._sift_up(parent)
