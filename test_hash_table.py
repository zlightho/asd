import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(10, 1)

    def test_hash_fun(self):
        index = self.hash_table.hash_fun("value")
        self.assertIsInstance(index, int)

    def test_seek_slot_empty(self):
        index = self.hash_table.seek_slot("value")
        self.assertIsInstance(index, int)

    def test_seek_slot_collisions(self):
        self.hash_table.put("value1")
        self.hash_table.put("value2")
        index = self.hash_table.seek_slot("value")
        self.assertIsInstance(index, int)

    def test_put_empty(self):
        index = self.hash_table.put("value")
        self.assertIsInstance(index, int)

    def test_put_collision(self):
        self.hash_table.put("value1")
        index = self.hash_table.put("value2")
        self.assertIsInstance(index, int)

    def test_put_full(self):
        for i in range(10):
            self.hash_table.put("value" + str(i))
        index = self.hash_table.put("value")
        self.assertIsNone(index)

    def test_find_empty(self):
        index = self.hash_table.find("value")
        self.assertIsNone(index)

    def test_find_existing(self):
        self.hash_table.put("value")
        index = self.hash_table.find("value")
        self.assertIsInstance(index, int)

    def test_find_not_existing(self):
        self.hash_table.put("value")
        index = self.hash_table.find("not_existing")
        self.assertIsNone(index)

if __name__ == "__main__":
    unittest.main()
