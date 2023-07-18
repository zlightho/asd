import unittest
from bloomfilter import BloomFilter


class TestFilterBloom(unittest.TestCase):
    def setUp(self):
        self.filter_bloom = BloomFilter(f_len=32)

    def test_add(self):
        strings = [
            "0123456789",
            "1234567890",
            "2345678901",
            "3456789012",
            "4567890123",
            "5678901234",
            "6789012345",
            "7890123456",
            "8901234567",
            "9012345678",
        ]

        for string in strings:
            self.filter_bloom.add(string)

        for string in strings:
            self.assertTrue(self.filter_bloom.is_value(string))


if __name__ == "__main__":
    unittest.main()
