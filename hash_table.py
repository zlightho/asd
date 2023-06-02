class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
        return sum(ord(c) for c in value) % self.size

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        index = self.hash_fun(value)
        while self.slots[index] is not None:
            index = (index + self.step) % self.size
        return index

    def put(self, value):
        # записываем значение по хэш-функции
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся разместить
        index = self.seek_slot(value)
        if self.slots[index] is None:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        # находит индекс слота со значением, или None
        index = self.hash_fun(value)
        while self.slots[index] is not None:
            if self.slots[index] == value:
                return index
            index = (index + self.step) % self.size
        return None
