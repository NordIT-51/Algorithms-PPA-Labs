import unittest


def maxnum(nums):
    nums = [str(num) for num in nums]
    maxlen = max(len(x) for x in nums)
    nums.sort(key=lambda x: x * (maxlen * 2), reverse=True)
    res = ''.join(nums)
    return '0' if res.lstrip('0') == '' else res



class TestLargestNumber(unittest.TestCase):
    def test1(self):
        # Пример из задачи
        digits = [21, 2]
        expected_output = '221'
        self.assertEqual(maxnum(digits), expected_output)

    def test2(self):
        # Пример из задачи
        digits = [23, 39, 92]
        expected_output = '923923'
        self.assertEqual(maxnum(digits), expected_output)

    def test_same_beginning(self):
        # Числа с одинаковым началом
        digits = [9, 91, 95, 93]
        expected_output = '9959391'
        self.assertEqual(maxnum(digits), expected_output)

    def test_single(self):
        # Однозначные числа
        digits = [5, 2, 1, 9, 7]
        expected_output = '97521'
        self.assertEqual(maxnum(digits), expected_output)

    def test_of_zeros(self):
        # Все нули
        digits = [0, 0, 0]
        expected_output = '0'
        self.assertEqual(maxnum(digits), expected_output)

    def test_large_numbers(self):
        # Относительно большие числа
        digits = [123, 1234, 12]
        expected_output = '123412312'
        self.assertEqual(maxnum(digits), expected_output)


if __name__ == '__main__':
    unittest.main()
