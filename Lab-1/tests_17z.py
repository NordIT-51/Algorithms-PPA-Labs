import unittest

moves = {
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
    0: [4, 6]
}

def count_horsenumbers(n):
    if n == 1:
        return 8
    elif n <= 0:
        raise ValueError('n некорректно')
    dp = [0] * 10
    new_dp = [0] * 10

    # телефонный номер не может начинаться ни c цифры 0, ни с цифры 8.
    for num in range(10):
        if num in [0, 5, 8]:
            continue
        dp[num] = 1

    for _ in range(2, n + 1):
        for num in range(10):
            new_dp[num] = 0

        for num in range(10):
            if dp[num] == 0:
                continue
            for move in moves.get(num, []):
                new_dp[move] = (new_dp[move] + dp[num]) % 10**9

        dp, new_dp = new_dp, dp

    res = sum(dp) % 10**9
    return res


class TestCountTelephoneNumbers(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_horsenumbers(1), 7)

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
