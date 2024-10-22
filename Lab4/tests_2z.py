from collections import defaultdict
import unittest

def count_palindromes(s):
    position_map = defaultdict(list)
    for idx, ch in enumerate(s):
        position_map[ch].append(idx)

    total_count = 0
    for positions in position_map.values():
        m = len(positions)
        if m < 2:
            continue
        total_pairs = m * (m - 1) // 2

        prefix_sums = [0] * m
        prefix_sums[0] = positions[0]
        for i in range(1, m):
            prefix_sums[i] = prefix_sums[i - 1] + positions[i]

        total_diff = 0
        for q in range(1, m):
            i_q = positions[q]
            total = i_q * q - prefix_sums[q - 1]
            total_diff += total

        total_c = total_diff - total_pairs
        total_count += total_c

    return total_count

class TestCountPalindromes(unittest.TestCase):
    def test_empty_string(self):
        # Пустая строка должна возвращать 0
        self.assertEqual(count_palindromes(''), 0)

    def test_single_character(self):
        # Строка из одного символа не содержит палиндромов длиной 3
        self.assertEqual(count_palindromes('a'), 0)

    def test_two_characters(self):
        # Строка из двух символов не содержит палиндромов длиной 3
        self.assertEqual(count_palindromes('ab'), 0)

    def test_no_palindromic_triplets(self):
        # В строке нет палиндромических триплетов
        self.assertEqual(count_palindromes('abc'), 0)

    def test_one_palindromic_triplet(self):
        # Строка содержит один палиндромический триплет
        self.assertEqual(count_palindromes('aba'), 1)

    def test_multiple_palindromic_triplets(self):
        # Строка содержит несколько палиндромических триплетов
        self.assertEqual(count_palindromes('ababa'), 6)

    def test_all_same_characters(self):
        # Строка из одинаковых символов
        self.assertEqual(count_palindromes('aaa'), 1)
        self.assertEqual(count_palindromes('aaaa'), 4)
        self.assertEqual(count_palindromes('aaaaa'), 10)

    def test_long_string(self):
        # Длинная строка для проверки производительности
        s = 'abcde' * 300 * 200  # Строка длиной 1000 символов
        result = count_palindromes(s)
        self.assertTrue(isinstance(result, int))
        self.assertGreaterEqual(result, 0)

    def test_palindromic_substrings(self):
        # Проверка с разными комбинациями символов
        self.assertEqual(count_palindromes('racecar'), 9)
        self.assertEqual(count_palindromes('level'), 4)

    def test_case_sensitivity(self):
        # Проверка чувствительности к регистру
        self.assertEqual(count_palindromes('AaA'), 1)  # 'A' != 'a' в разных регистрах

    def test_non_alphabetic_characters(self):
        # Строка с неалфавитными символами
        self.assertEqual(count_palindromes('12321'), 4)
        self.assertEqual(count_palindromes('!@#@!'), 4)

if __name__ == '__main__':
    unittest.main()