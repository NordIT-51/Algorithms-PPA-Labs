import unittest

def longest_common_substring(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0
    end_pos_s = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos_s = i

    start_pos_s = end_pos_s - max_length
    start_pos_t = -1
    for j in range(n):
        if s[start_pos_s:start_pos_s + max_length] == t[j:j + max_length]:
            start_pos_t = j
            break

    return s[start_pos_s:end_pos_s], start_pos_s, start_pos_t, max_length


class TestLongestCommonSubstring(unittest.TestCase):
    def test_common_case(self):
        s = "abcdef"
        t = "zbcdf"
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "bcd")
        self.assertEqual(start_s, 1)
        self.assertEqual(start_t, 1)
        self.assertEqual(length, 3)

    def test_full_match(self):
        s = "hello"
        t = "hello"
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "hello")
        self.assertEqual(start_s, 0)
        self.assertEqual(start_t, 0)
        self.assertEqual(length, 5)

    def test_no_common_substring(self):
        s = "abc"
        t = "def"
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "")
        self.assertEqual(start_s, 0)
        self.assertEqual(start_t, 0)
        self.assertEqual(length, 0)

    def test_empty_strings(self):
        s = ""
        t = ""
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "")
        self.assertEqual(start_s, 0)
        self.assertEqual(start_t, -1)
        self.assertEqual(length, 0)

    def test_one_empty_string(self):
        s = "abc"
        t = ""
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "")
        self.assertEqual(start_s, 0)
        self.assertEqual(start_t, -1)
        self.assertEqual(length, 0)

    def test_repeated_characters(self):
        s = "aaaaa"
        t = "aaa"
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "aaa")
        self.assertEqual(start_s, 0)
        self.assertEqual(start_t, 0)
        self.assertEqual(length, 3)

    def test_substring_at_end(self):
        s = "abcde"
        t = "cde"
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "cde")
        self.assertEqual(start_s, 2)
        self.assertEqual(start_t, 0)
        self.assertEqual(length, 3)

    def test_substring_at_beginning(self):
        s = "hello world"
        t = "hello"
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "hello")
        self.assertEqual(start_s, 0)
        self.assertEqual(start_t, 0)
        self.assertEqual(length, 5)

    def test_unicode_characters(self):
        s = "こんにちは"
        t = "こんばんは"
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "こん")
        self.assertEqual(start_s, 0)
        self.assertEqual(start_t, 0)
        self.assertEqual(length, 2)

    def test_overlapping_substrings(self):
        s = "abababa"
        t = "babab"
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "babab")
        self.assertEqual(start_s, 1)
        self.assertEqual(start_t, 0)
        self.assertEqual(length, 5)

    def test_long_strings(self):
        s = "a" * 1000 + "b"
        t = "a" * 1000 + "c"
        substring, start_s, start_t, length = longest_common_substring(s, t)
        self.assertEqual(substring, "a" * 1000)
        self.assertEqual(start_s, 0)
        self.assertEqual(start_t, 0)
        self.assertEqual(length, 1000)

if __name__ == "__main__":
    unittest.main()
