import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task_17z import count_horsenumbers


class TestCountTelephoneNumbers(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_horsenumbers(1), 8)

    def test2(self):
        expected_result = 16
        self.assertEqual(count_horsenumbers(2), expected_result)

    def test3(self):
        expected_result = 36
        self.assertEqual(count_horsenumbers(3), expected_result)

    def test4(self):
        expected_result = 82
        self.assertEqual(count_horsenumbers(4), expected_result)

    def test_large(self):
        n = 10
        expected_result = count_horsenumbers(10)
        self.assertEqual(count_horsenumbers(10), expected_result)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            count_horsenumbers(0)


if __name__ == '__main__':
    unittest.main()
