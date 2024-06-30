import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


import unittest
from main_tasks.bbstarray import GenerateBBSTArray


class TestGenerateBBSTArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(GenerateBBSTArray([]), [])

    def test_single_element_array(self):
        self.assertEqual(GenerateBBSTArray([10]), [10])

    def test_two_elements_array(self):
        self.assertEqual(GenerateBBSTArray([10, 20]), [20, 10, None])

    def test_three_elements_array(self):
        self.assertEqual(GenerateBBSTArray([10, 20, 30]), [20, 10, 30])

    def test_multiple_elements_array(self):
        input_array = [3, 1, 4, 1, 5, 9, 2]
        result = GenerateBBSTArray(input_array)
        expected_output = [3, 1, 5, 1, 2, 4, 9]
        self.assertEqual(result, expected_output)

    def test_sorted_array(self):
        input_array = [1, 2, 3, 4, 5, 6, 7]
        result = GenerateBBSTArray(input_array)
        expected_output = [4, 2, 6, 1, 3, 5, 7]
        self.assertEqual(result, expected_output)

    def test_reverse_sorted_array(self):
        input_array = [7, 6, 5, 4, 3, 2, 1]
        result = GenerateBBSTArray(input_array)
        expected_output = [4, 2, 6, 1, 3, 5, 7]
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
