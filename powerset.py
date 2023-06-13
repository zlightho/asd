# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        # ваша реализация хранилища
        self.items = []

    def size(self):
        return len(self.items)
        # количество элементов в множестве

    def put(self, value):
        # всегда срабатывает
        self.items.append(value)

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        return value in self.items

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        if value in self.items:
            self.items.remove(value)
            return True
        return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        result = PowerSet()
        for value in self.items:
            if set2.get(value):
                result.put(value)
        return result

    def union(self, set2):
        # объединение текущего множества и set2
        result = PowerSet()
        for value in self.items:
            result.put(value)
        for value in set2.items:
            result.put(value)
        return result

    def difference(self, set2):
        # разница текущего множества и set2
        result = PowerSet()
        for value in self.items:
            if not set2.get(value):
                result.put(value)
        return result

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for value in set2.items:
            if not self.get(value):
                return False
        return True