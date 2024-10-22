import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task_8z import max_lectures


def max_lectures(requests):
    requests.sort(key=lambda x: x[1])
    count = 0
    last_end = 0
    for start, end in requests:
        if start >= last_end:
            last_end = end
            count += 1
    return count


class TestMaxLectures(unittest.TestCase):
    def test1(self):
        # Пример из задачи
        requests = [(5, 10)]
        expected_output = 1
        self.assertEqual(max_lectures(requests), expected_output)

    def test2(self):
        # Пример из задачи
        requests = [(1, 5), (2, 3), (3, 4)]
        expected_output = 2
        self.assertEqual(max_lectures(requests), expected_output)

    def test_no_lectures(self):
        # Лекции отсутствуют
        requests = []
        expected_output = 0
        self.assertEqual(max_lectures(requests), expected_output)

    def test_overlapping_lectures(self):
        # Полностью перекрывающиеся лекции
        requests = [(1, 4), (2, 5), (3, 6)]
        expected_output = 1
        self.assertEqual(max_lectures(requests), expected_output)

    def test_non_overlapping_lectures(self):
        # Непересекающиеся лекции
        requests = [(1, 2), (3, 4), (5, 6)]
        expected_output = 3
        self.assertEqual(max_lectures(requests), expected_output)

    def test_same_end_times(self):
        # Лекции с одинаковым временем окончания
        requests = [(1, 3), (2, 3), (3, 3)]
        expected_output = 2
        self.assertEqual(max_lectures(requests), expected_output)


if __name__ == '__main__':
    unittest.main()
