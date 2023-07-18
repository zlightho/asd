class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = [0] * f_len

    def hash1(self, str1):
        # 17
        code = 0
        for c in str1:
            code = (code * 17 + ord(c)) % self.filter_len
        return code

    def hash2(self, str1):
        # 223
        code = 0
        for c in str1:
            code = (code * 223 + ord(c)) % self.filter_len
        return code

    def add(self, str1):
        # Добавление строки в фильтр
        index = self.hash1(str1)
        self.bit_array[index] = 1

    def is_value(self, str1):
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)
        return self.bit_array[index1] == 1 and self.bit_array[index2] == 1
