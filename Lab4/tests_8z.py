import unittest

def find_approximate_matches(k, t, p):
    matches = []
    len_t = len(t)
    len_p = len(p)
    for i in range(len_t - len_p + 1):
        mismatch_count = sum(1 for j in range(len_p) if t[i + j] != p[j])
        if mismatch_count <= k:
            matches.append(i)
    return matches

class TestFindApproximateMatches(unittest.TestCase):
    def test_exact_match(self):
        k = 0
        t = "abcdeabcde"
        p = "abc"
        expected = [0, 5]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_no_match(self):
        k = 0
        t = "abcdeabcde"
        p = "xyz"
        expected = []
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_single_mismatch(self):
        k = 1
        t = "abcdeabcde"
        p = "abf"
        expected = [0, 5]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_multiple_mismatches_allowed(self):
        k = 2
        t = "abcdefghij"
        p = "abkde"
        expected = [0]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_k_equals_pattern_length(self):
        k = 5
        t = "abcdefghij"
        p = "klmno"
        expected = [0, 1, 2, 3, 4, 5]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_empty_text(self):
        k = 0
        t = ""
        p = "abc"
        expected = []
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_empty_pattern(self):
        k = 0
        t = "abcde"
        p = ""
        expected = [0, 1, 2, 3, 4, 5]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_both_empty(self):
        k = 0
        t = ""
        p = ""
        expected = [0]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_non_ascii_characters(self):
        k = 1
        t = "Приветмир"
        p = "Провет"
        expected = [0]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_overlapping_matches(self):
        k = 1
        t = "aaaaaa"
        p = "aaa"
        expected = [0, 1, 2, 3]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_large_k(self):
        k = 100
        t = "abcdef"
        p = "xyz"
        expected = [0, 1, 2, 3]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_k_greater_than_pattern_length(self):
        k = 10
        t = "abcdefgh"
        p = "abc"
        expected = [0, 1, 2, 3, 4, 5]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_case_sensitivity(self):
        k = 1
        t = "AbCdEfGh"
        p = "abcdefg"
        expected = []
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_numeric_strings(self):
        k = 1
        t = "1234512345"
        p = "123"
        expected = [0, 5]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_special_characters(self):
        k = 1
        t = "@#$%^&*()"
        p = "%^&"
        expected = [3]
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_long_text_short_pattern(self):
        k = 0
        t = "a" * 1000
        p = "a"
        expected = list(range(1000))
        result = find_approximate_matches(k, t, p)
        self.assertEqual(result, expected)

    def test_long_pattern(self):
        import unittest

        def find_approximate_matches(k, t, p):
            matches = []
            len_t = len(t)
            len_p = len(p)
            for i in range(len_t - len_p + 1):
                mismatch_count = sum(1 for j in range(len_p) if t[i + j] != p[j])
                if mismatch_count <= k:
                    matches.append(i)
            return matches

        class TestFindApproximateMatches(unittest.TestCase):
            def test_exact_match(self):
                k = 0
                t = "abcdeabcde"
                p = "abc"
                expected = [0, 5]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_no_match(self):
                k = 0
                t = "abcdeabcde"
                p = "xyz"
                expected = []
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_single_mismatch(self):
                k = 1
                t = "abcdeabcde"
                p = "abf"
                expected = [0, 5]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_multiple_mismatches_allowed(self):
                k = 2
                t = "abcdefghij"
                p = "abkde"
                expected = [0]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_k_equals_pattern_length(self):
                k = 5
                t = "abcdefghij"
                p = "klmno"
                expected = [0, 1, 2, 3, 4, 5]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_empty_text(self):
                k = 0
                t = ""
                p = "abc"
                expected = []
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_empty_pattern(self):
                k = 0
                t = "abcde"
                p = ""
                expected = [0, 1, 2, 3, 4, 5]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_both_empty(self):
                k = 0
                t = ""
                p = ""
                expected = [0]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_non_ascii_characters(self):
                k = 1
                t = "Приветмир"
                p = "Провет"
                expected = [0]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_overlapping_matches(self):
                k = 1
                t = "aaaaaa"
                p = "aaa"
                expected = [0, 1, 2, 3]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_large_k(self):
                k = 100
                t = "abcdef"
                p = "xyz"
                expected = [0, 1, 2, 3]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_k_greater_than_pattern_length(self):
                k = 10
                t = "abcdefgh"
                p = "abc"
                expected = [0, 1, 2, 3, 4, 5]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_case_sensitivity(self):
                k = 1
                t = "AbCdEfGh"
                p = "abcdefg"
                expected = []
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_numeric_strings(self):
                k = 1
                t = "1234512345"
                p = "123"
                expected = [0, 5]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_special_characters(self):
                k = 1
                t = "@#$%^&*()"
                p = "%^&"
                expected = [3]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_long_text_short_pattern(self):
                k = 0
                t = "a" * 1000
                p = "a"
                expected = list(range(1000))
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            def test_long_pattern(self):
                k = 2
                t = "abcdefghij"
                p = "abcdxyzefg"
                expected = [0]
                result = find_approximate_matches(k, t, p)
                self.assertEqual(result, expected)

            if __name__ == '__main__':
                unittest.main()