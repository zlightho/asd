class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return sum(ord(c) for c in key) % self.size

    def is_key(self, key):
        index = self.hash_fun(key)
        return self.slots[index] == key

    def put(self, key, value):
        index = self.hash_fun(key)

        if None in self.slots:
            while self.slots[index] is not None:
                index = (index + 1) % self.size
        else:
            min_hits_index = self.hits.index(min(self.hits))
            index = min_hits_index

        self.slots[index] = key
        self.values[index] = value
        self.hits[index] = 0

    def get(self, key):
        index = self.hash_fun(key)
        start_index = index

        while self.slots[index] is not None:
            if self.slots[index] == key:
                self.hits[index] += 1
                return self.values[index]
            index = (index + 1) % self.size
            if index == start_index:
                break

        return None
