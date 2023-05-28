import unittest
from ordered_list import OrderedList, OrderedStringList

class TestOrderedList(unittest.TestCase):
    def setUp(self):
        self.ordered_list_asc = OrderedList(asc=True)
        self.ordered_list_desc = OrderedList(asc=False)
        self.ordered_string_list_asc = OrderedStringList(asc=True)
        self.ordered_string_list_desc = OrderedStringList(asc=False)

    def test_add_asc(self):
        self.ordered_list_asc.add(3)
        self.ordered_list_asc.add(1)
        self.ordered_list_asc.add(2)
        self.assertEqual(self.ordered_list_asc.get_all(), [1, 2, 3])

    def test_add_desc(self):
        self.ordered_list_desc.add(3)
        self.ordered_list_desc.add(1)
        self.ordered_list_desc.add(2)
        self.assertEqual(self.ordered_list_desc.get_all(), [3, 2, 1])

    def test_add_string_asc(self):
        self.ordered_string_list_asc.add("apple")
        self.ordered_string_list_asc.add("banana")
        self.ordered_string_list_asc.add("cherry")
        self.assertEqual(self.ordered_string_list_asc.get_all(), ["apple", "banana", "cherry"])

    def test_add_string_desc(self):
        self.ordered_string_list_desc.add("apple")
        self.ordered_string_list_desc.add("banana")
        self.ordered_string_list_desc.add("cherry")
        self.assertEqual(self.ordered_string_list_desc.get_all(), ["cherry", "banana", "apple"])

    def test_find(self):
        self.ordered_list_asc.add(3)
        self.ordered_list_asc.add(1)
        self.ordered_list_asc.add(2)
        self.assertEqual(self.ordered_list_asc.find(2).value, 2)
        self.assertIsNone(self.ordered_list_asc.find(4))

    def test_find_string(self):
        self.ordered_string_list_asc.add("apple")
        self.ordered_string_list_asc.add("banana")
        self.ordered_string_list_asc.add("cherry")
        self.assertEqual(self.ordered_string_list_asc.find("banana").value, "banana")
        self.assertIsNone(self.ordered_string_list_asc.find("orange"))

    def test_delete(self):
        self.ordered_list_asc.add(3)
        self.ordered_list_asc.add(1)
        self.ordered_list_asc.add(2)
        self.ordered_list_asc.delete(2)
        self.assertEqual(self.ordered_list_asc.get_all(), [1, 3])

    def test_delete_string(self):
        self.ordered_string_list_asc.add("apple")
        self.ordered_string_list_asc.add("banana")
        self.ordered_string_list_asc.add("cherry")
        self.ordered_string_list_asc.delete("banana")
        self.assertEqual(self.ordered_string_list_asc.get_all(), ["apple", "cherry"])

    def test_clean(self):
        self.ordered_list_asc.add(3)
        self.ordered_list_asc.add(1)
        self.ordered_list_asc.add(2)
        self.ordered_list_asc.clean(asc=False)
        self.assertEqual(self.ordered_list_asc.get_all(), [])

    def test_clean_string(self):
        self.ordered_string_list_asc.add("apple")
        self.ordered_string_list_asc.add("banana")
        self.ordered_string_list_asc.add("cherry")
        self.ordered_string_list_asc.clean(asc=False)
        self.assertEqual(self.ordered_string_list_asc.get_all(), [])

    def test_len(self):
        self.assertEqual(self.ordered_list_asc.len(), 0)
        self.ordered_list_asc.add(3)
        self.assertEqual(self.ordered_list_asc.len(), 1)
        self.ordered_list_asc.add(1)
        self.assertEqual(self.ordered_list_asc.len(), 2)
        self.ordered_list_asc.delete(3)
        self.assertEqual(self.ordered_list_asc.len(), 1)
        self.ordered_list_asc.delete(1)
        self.assertEqual(self.ordered_list_asc.len(), 0)

    def test_len_string(self):
        self.assertEqual(self.ordered_string_list_asc.len(), 0)
        self.ordered_string_list_asc.add("apple")
        self.assertEqual(self.ordered_string_list_asc.len(), 1)
        self.ordered_string_list_asc.add("banana")
        self.assertEqual(self.ordered_string_list_asc.len(), 2)
        self.ordered_string_list_asc.delete("apple")
        self.assertEqual(self.ordered_string_list_asc.len(), 1)
        self.ordered_string_list_asc.delete("banana")
        self.assertEqual(self.ordered_string_list_asc.len(), 0)

if __name__ == "__main__":
    unittest.main()
