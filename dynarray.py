import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        """добавляем объект itm в позицию i, начиная с 0
        сложность - O(n) в худшем случае нам приходится сдвигать
        все элементы массива после вставляемого элемента."""
        if i < 0 or i > self.count:
            raise IndexError("Index is out of bounds")
        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        for j in range(self.count - 1, i - 1, -1):
            self.array[j + 1] = self.array[j]

        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        """удаляем объект в позиции i
        сложность - O(n) в худшем случае нам приходится сдвигать
        все элементы массива после удаленного элемента."""
        if self.count == 0:
            raise IndexError("Index is out of bounds")

        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")

        if i == self.count - 1:
            self.array[i] = 0
            self.count -= 1
            return
        else:
            for j in range(i, self.count - 1):
                self.array[j] = self.array[j + 1]

            self.array[self.count - 1] = 0
            self.count -= 1
        # проверяем заполненность буфера после удаления
        if self.capacity > 16 and self.count < self.capacity // 2:
            new_capacity = max(16, int(self.capacity / 1.5))
            self.resize(new_capacity)
