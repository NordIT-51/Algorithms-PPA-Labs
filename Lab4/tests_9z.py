import unittest

def decompose(s):
    n = len(s)
    dp = [[''] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = s[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = s[i:j + 1]
            for k in range(i, j):
                combined = dp[i][k] + '+' + dp[k + 1][j]
                if len(combined) < len(dp[i][j]):
                    dp[i][j] = combined
            substr = s[i:j + 1]
            substr_len = len(substr)
            for l in range(1, substr_len // 2 + 1):
                if substr_len % l == 0:
                    times = substr_len // l
                    pattern = substr[0:l]
                    if pattern * times == substr:
                        candidate = dp[i][i + l - 1] + '*' + str(times)
                        if len(candidate) < len(dp[i][j]):
                            dp[i][j] = candidate
    return dp[0][n - 1] if n > 0 else ''

class TestDecomposeFunction(unittest.TestCase):

    def test_empty_string(self):
        s = ""
        expected = ""
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "a"
        expected = "a"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_no_repeats(self):
        s = "abcde"
        expected = "abcde"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_simple_repeat(self):
        s = "aaaaaa"
        expected = "a*6"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_simple_repeat_same_length(self):
        s = "aaa"
        expected = "aaa"  # Since 'aaa' and 'a*3' are same length, original string is chosen
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_complex_repeat(self):
        s = "ababab"
        expected = "ab*3"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_no_compression(self):
        s = "abcdefg"
        expected = "abcdefg"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_long_repeat(self):
        s = "a" * 100
        expected = "a*100"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_multiple_substrings(self):
        s = "abcabcabcabc"
        expected = "abc*4"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_mixed_characters(self):
        s = "aabbaabb"
        expected = "aabb*2"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_nested_repeats(self):
        s = "aaabaaab"
        expected = "aaab*2"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_alternating_pattern(self):
        s = "abcdabcdabcd"
        expected = "abcd*3"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_long_non_repeating_string(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        expected = "abcdefghijklmnopqrstuvwxyz"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_repeating_substrings(self):
        s = "abcabcabcabcabcabcabcabcabcabc"
        expected = "abc*10"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_numbers_in_string(self):
        s = "123123123123"
        expected = "123*4"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_complex_mixed_pattern(self):
        s = "abcabcabcdabcd"
        expected = "abc*3+dabcd"  # No shorter representation found
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_non_exact_repeats(self):
        s = "abababcabababc"
        expected = "ab*3+c*2"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_single_character_repeats(self):
        s = "bbbbbb"
        expected = "b*6"
        result = decompose(s)
        self.assertEqual(result, expected)

    def test_combined_repeats_and_additions(self):
        s = "aaaaabaaaaab"
        expected = "a*5+b*2"
        result = decompose(s)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
