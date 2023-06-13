import unittest
import time
from powerset import PowerSet

class PowerSetTests(unittest.TestCase):
    def setUp(self):
        self.set1 = PowerSet()
        self.set2 = PowerSet()

    def test_put(self):
        for i in range(10):
            self.set1.put(i)
            self.assertEqual(self.set1.get(i), True)
            self.assertEqual(self.set1.get(i + 10), False)
            self.assertEqual(self.set1.size(), i + 1)  # Добавьте эту строку
            
        self.assertIsNone(self.set1.put(10))
        self.assertEqual(self.set1.get(10), True)
        self.assertEqual(self.set1.size(), 11)  # Добавьте эту строку

        self.assertIsNone(self.set1.put(10))
        self.assertEqual(self.set1.size(), 12)


    def test_remove(self):
        for i in range(10):
            self.set1.put(i)

        for i in range(5):
            self.assertEqual(self.set1.remove(i), True)

        for i in range(5):
            self.assertEqual(self.set1.get(i), False)
        for i in range(5, 10):
            self.assertEqual(self.set1.get(i), True)

    def test_difference(self):
        self.set1.put(123)
        self.set1.put(234)
        self.set1.put(567)
        self.set1.put(789)
        self.set2.put(234)
        self.set2.put(456)
        self.set2.put(567)
        self.set2.put(678)

        difference = self.set1.difference(self.set2)
        self.assertEqual(4, self.set1.size())
        self.assertEqual(4, self.set2.size())
        self.assertEqual(2, difference.size())
        self.assertEqual([123, 789], difference.items)

    def test_union(self):
        union = self.set1.union(self.set2)
        self.assertEqual(union.size(), 0)

        for i in range(5):
            self.set1.put(i)
        self.set2.put(5)
        self.set2.put(6)
        union = self.set1.union(self.set2)
        self.assertEqual(union.size(), 7)
        self.assertEqual(union.get(0), True)
        self.assertEqual(union.get(1), True)
        self.assertEqual(union.get(2), True)
        self.assertEqual(union.get(3), True)
        self.assertEqual(union.get(4), True)
        self.assertEqual(union.get(5), True)
        self.assertEqual(union.get(6), True)

        empty_set = PowerSet()
        union_with_empty = self.set1.union(empty_set)
        self.assertEqual(union_with_empty.size(), self.set1.size())


    def test_intersection(self):
        self.set1.put(123)
        self.set1.put(234)
        self.set1.put(345)
        self.set2.put(456)

        intersection = self.set2.intersection(self.set2)
        self.assertEqual(3, self.set1.size())
        self.assertEqual(1, self.set2.size())
        self.assertEqual(1, intersection.size())

        self.set2.put(234)
        self.set2.put(345)
        intersection = self.set1.intersection(self.set2)
        self.assertEqual(3, self.set2.size())
        self.assertEqual(2, intersection.size())
        self.assertEqual([234, 345], intersection.items)


    
    def test_performance(self):
        for i in range(20000):
            self.set1.put(i)
            self.set2.put(i + 10000)

        start_time = time.time()
        intersection = self.set1.intersection(self.set2)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLessEqual(execution_time, 2.0, f"Intersection execution time: {execution_time:.2f} sec")

        start_time = time.time()
        union = self.set1.union(self.set2)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLessEqual(execution_time, 2.0, f"Union execution time: {execution_time:.2f} sec")

        start_time = time.time()
        difference = self.set1.difference(self.set2)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLessEqual(execution_time, 2.0, f"Difference execution time: {execution_time:.2f} sec")

        start_time = time.time()
        self.set1.issubset(self.set2)
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLessEqual(execution_time, 2.0, f"Subset execution time: {execution_time:.2f} sec")

if __name__ == "__main__":
    unittest.main()
