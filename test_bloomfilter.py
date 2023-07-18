import unittest
from bloomfilter import BloomFilter


class TestFilterBloom(unittest.TestCase):
    def setUp(self):
        self.filter_bloom = BloomFilter(32)


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

    self.assertFalse(self.filter_bloom.is_value("not_added_string"))


def test_false_positive(self):
    test_strings = [
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
    non_existing_strings = [
        "9876543210",
        "0987654321",
        "9876543210",
        "0987654321",
        "9876543210",
        "0987654321",
        "9876543210",
        "0987654321",
        "9876543210",
        "0987654321",
    ]
    for string in test_strings:
        self.filter_bloom.add(string)

    for string in non_existing_strings:
        self.assertFalse(self.filter_bloom.is_value(string))


if __name__ == "__main__":
    unittest.main()
