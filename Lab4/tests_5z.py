import unittest

def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

class TestPrefixFunction(unittest.TestCase):
    def test_empty_string(self):
        """Тест пустой строки."""
        s = ''
        expected = []
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        """Тест строки из одного символа."""
        s = 'a'
        expected = [0]
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

    def test_no_repeats(self):
        """Тест строки без повторяющихся префиксов."""
        s = 'abcdef'
        expected = [0, 0, 0, 0, 0, 0]
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

    def test_simple_repeat(self):
        """Тест строки с простым повторением."""
        s = 'aa'
        expected = [0, 1]
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

    def test_complex_string(self):
        """Тест сложной строки с повторяющимися префиксами."""
        s = 'ababcababd'
        expected = [0, 0, 1, 2, 0, 1, 2, 3, 4, 0]
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

    def test_full_repeat(self):
        """Тест строки с полным повторением символов."""
        s = 'aaaaa'
        expected = [0, 1, 2, 3, 4]
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

    def test_partial_repeat(self):
        """Тест строки с частичным повторением."""
        s = 'abcab'
        expected = [0, 0, 0, 1, 2]
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

    def test_unicode_characters(self):
        """Тест строки с Unicode-символами."""
        s = 'абаба'
        expected = [0, 0, 1, 2, 3]
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

    def test_mixed_characters(self):
        """Тест строки с различными символами."""
        s = 'aabaabaaa'
        expected = [0, 1, 0, 1, 2, 3, 4, 5, 2]
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

    def test_long_string(self):
        """Тест длинной строки."""
        s = 'abcdabcabcdabcdab'
        expected = [0, 0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 4, 5, 6]
        result = compute_prefix_function(s)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
