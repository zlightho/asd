import unittest
from dynarray import DynArray


class TestDynArray(unittest.TestCase):
    def setUp(self):
        self.da = DynArray()
        for i in range(16):
            self.da.append(i)

    def test_insert_within_capacity(self):
        self.da.insert(5, 100)
        self.assertEqual(self.da.count, 17)
        self.assertEqual(self.da[5], 100)
        self.assertEqual(self.da[6], 5)

    def test_insert_exceed_capacity(self):
        for i in range(16, 32):
            self.da.append(i)
        self.assertEqual(self.da.count, 32)
        self.assertEqual(self.da.capacity, 32)
        self.da.insert(25, 200)
        self.assertEqual(self.da.count, 33)
        self.assertEqual(self.da.capacity, 64)
        self.assertEqual(self.da[25], 200)
        self.assertEqual(self.da[26], 25)

    def test_insert_invalid_position(self):
        with self.assertRaises(IndexError):
            self.da.insert(-1, 100)
        with self.assertRaises(IndexError):
            self.da.insert(100, 100)

    def test_delete_within_capacity(self):
        self.da.delete(5)
        self.assertEqual(self.da.count, 15)
        self.assertEqual(self.da[5], 6)

    def test_delete_shrink_capacity(self):
        for i in range(8):
            self.da.delete(0)
        self.assertEqual(self.da.count, 8)
        self.assertEqual(self.da.capacity, 16)
        self.da.delete(0)
        self.assertEqual(self.da.count, 7)
        self.assertEqual(self.da.capacity, 16)

    def test_delete_invalid_position(self):
        with self.assertRaises(IndexError):
            self.da.delete(-1)
        with self.assertRaises(IndexError):
            self.da.delete(100)


if __name__ == "__main__":
    unittest.main()
