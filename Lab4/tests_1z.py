import unittest

def find_substrings(p, t):
    occurrences = []
    p_len = len(p)
    for i in range(len(t) - p_len + 1):
        if t[i:i + p_len] == p:
            occurrences.append(i + 1)
    return occurrences

class TestFindSubstrings(unittest.TestCase):
    def test_no_match(self):
        """Тест на отсутствие совпадений."""
        p = "abc"
        t = "defghijkl"
        result = find_substrings(p, t)
        self.assertEqual(result, [])

    def test_single_match(self):
        """Тест с одним совпадением в начале строки."""
        p = "abc"
        t = "abcdefgh"
        result = find_substrings(p, t)
        self.assertEqual(result, [1])

    def test_single_match_middle(self):
        """Тест с одним совпадением в середине строки."""
        p = "def"
        t = "abcdefghi"
        result = find_substrings(p, t)
        self.assertEqual(result, [4])

    def test_single_match_end(self):
        """Тест с одним совпадением в конце строки."""
        p = "ghi"
        t = "abcdefghi"
        result = find_substrings(p, t)
        self.assertEqual(result, [7])

    def test_multiple_matches(self):
        """Тест с несколькими неперекрывающимися совпадениями."""
        p = "ab"
        t = "abxabxab"
        result = find_substrings(p, t)
        self.assertEqual(result, [1, 4, 7])

    def test_overlapping_matches(self):
        """Тест с перекрывающимися совпадениями."""
        p = "aa"
        t = "aaaaa"
        result = find_substrings(p, t)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_empty_pattern(self):
        """Тест с пустым образцом."""
        p = ""
        t = "abc"
        result = find_substrings(p, t)
        expected = [1, 2, 3, 4]  # Пустая строка считается совпадением в каждом положении
        self.assertEqual(result, expected)

    def test_empty_text(self):
        """Тест с пустым текстом."""
        p = "abc"
        t = ""
        result = find_substrings(p, t)
        self.assertEqual(result, [])

    def test_both_empty(self):
        """Тест с пустым образцом и пустым текстом."""
        p = ""
        t = ""
        result = find_substrings(p, t)
        self.assertEqual(result, [1])

    def test_case_sensitivity(self):
        """Тест на чувствительность к регистру."""
        p = "abc"
        t = "AbcabcABC"
        result = find_substrings(p, t)
        self.assertEqual(result, [4])

    def test_special_characters(self):
        """Тест с специальными символами."""
        p = "@#"
        t = "123@#456@#"
        result = find_substrings(p, t)
        self.assertEqual(result, [4, 9])

    def test_unicode_characters(self):
        """Тест с использованием Unicode символов."""
        p = "тест"
        t = "этотесттестовыйтест"
        result = find_substrings(p, t)
        self.assertEqual(result, [4, 8, 16])

if __name__ == "__main__":
    unittest.main()
