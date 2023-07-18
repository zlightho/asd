class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = 0

    def hash1(self, str1):
        code = 0
        for c in str1:
            code = (code * 17 + ord(c)) % self.filter_len
        return code

    def hash2(self, str1):
        code = 0
        for c in str1:
            code = (code * 223 + ord(c)) % self.filter_len
        return code

    def add(self, str1):
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)
        self.bit_array |= (1 << index1) | (1 << index2)

    def is_value(self, str1):
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)
        return (self.bit_array & (1 << index1)) != 0 and (
            self.bit_array & (1 << index2)
        ) != 0
