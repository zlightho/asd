import native_cache
import unittest


class NativeCacheTests(unittest.TestCase):
    def test_cache_overflow_with_hits(self):
        cache = native_cache.NativeCache(5)
        keys = ["first", "second", "third", "fourth", "fifth"]
        values = [34, 4, 424, 43, 24]

        for key, value in zip(keys, values):
            cache.put(key, value)

        cache.get("first")
        cache.get("second")
        cache.get("third")
        cache.get("fourth")

        cache.put("sixth", 10)

        expected_slots = ["first", "second", "third", "fourth", "sixth"]
        expected_values = [34, 4, 424, 43, 10]

        self.assertCountEqual(cache.slots, expected_slots)
        self.assertCountEqual(cache.values, expected_values)
        self.assertEqual(cache.hits[cache.hash_fun("first")], 1)
        self.assertEqual(cache.hits[cache.hash_fun("fifth")], 1)

    def test_cache_hit_count(self):
        cache = native_cache.NativeCache(5)
        cache.put("one", 1)
        cache.put("two", 2)
        cache.put("three", 3)

        cache.get("one")
        cache.get("one")
        cache.get("two")

        self.assertEqual(cache.hits[cache.hash_fun("one")], 2)
        self.assertEqual(cache.hits[cache.hash_fun("two")], 1)


if __name__ == "__main__":
    unittest.main()
