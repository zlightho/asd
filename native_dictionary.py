class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        return sum(ord(c) for c in key) % self.size

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        index = self.hash_fun(key)
        return self.slots[index] == key

    def put(self, key, value):
        # гарантированно записываем
        # значение value по ключу key
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = value


    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден
        index = self.hash_fun(key)  
        if self.slots[index] == key:
            return self.values[index]
        return None
