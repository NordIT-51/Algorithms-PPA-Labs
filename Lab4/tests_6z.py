import unittest


def compute_z_function(s):
    n = len(s)
    if n==0:
        return [0]
    z = [0] * n
    l, r, z[0] = 0, 0, n

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z

class TestZFunction(unittest.TestCase):
    def test_empty_string(self):
        s = ""
        expected_z = [0]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

    def test_single_character(self):
        s = "a"
        expected_z = [1]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

    def test_all_same_characters(self):
        s = "aaaaaa"
        expected_z = [6, 5, 4, 3, 2, 1]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

    def test_no_repeats(self):
        s = "abcdef"
        expected_z = [6, 0, 0, 0, 0, 0]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

    def test_repeats(self):
        s = "abcabcabc"
        expected_z = [9, 0, 0, 6, 0, 0, 3, 0, 0]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

    def test_prefix_suffix(self):
        s = "aabaaab"
        expected_z = [7, 1, 0, 2, 3, 1, 0]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

    def test_long_string(self):
        s = "abacabadabacabae"
        expected_z = [16, 0, 1, 0, 3, 0, 1, 0, 7, 0, 1, 0, 3, 0, 1, 0]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

    def test_random_string(self):
        s = "aabcaabxbaaz"
        expected_z = [12, 1, 0, 0, 3, 1, 0, 0, 0, 2, 1, 0]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

    def test_palindrome(self):
        s = "abcba"
        expected_z = [5, 0, 0, 0, 1]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

    def test_mixed_characters(self):
        s = "aabxaaazaaab"
        expected_z = [12, 1, 0, 0, 2, 2, 1, 0, 2, 3, 1, 0]
        result_z = compute_z_function(s)
        self.assertEqual(result_z, expected_z)

if __name__ == '__main__':
    unittest.main()
