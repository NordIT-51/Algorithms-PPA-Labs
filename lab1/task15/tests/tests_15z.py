import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task_15z import isMatching, repair_brackets

class TestRepairBrackets(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(repair_brackets(''), '', "Должен вернуть пустую строку из-за пустого ввода")

    def test_no_brackets(self):
        self.assertEqual(repair_brackets('hello world'), 'hello world', "Должен вернуть ту же строку, если нет скобок")

    def test_already_balanced(self):
        self.assertEqual(repair_brackets('a(b)c[d]{e}'), 'a(b)c[d]{e}', "Должен вернуть ту же строку, так как скобки сбалансированы")

    def test_unbalanced_left_brackets(self):
        self.assertEqual(repair_brackets('((('), '', "Должен удалить все несоответствующие открывающиеся скобки")
        self.assertEqual(repair_brackets('((a'), 'a', "Должен удалить несоответствующие открывающиеся скобки и сохранить другие символы")

    def test_unbalanced_right_brackets(self):
        self.assertEqual(repair_brackets(')))'), '', "Должен удалить все несоответствующие закрывающиеся скобки")
        self.assertEqual(repair_brackets('a)))'), 'a', "Должен удалить несоответствующие закрывающиеся скобки и сохранить другие символы")

    def test_nested_brackets(self):
        self.assertEqual(repair_brackets('a(b(c)d)e'), 'a(b(c)d)e', "Должен обрабатывать вложенные скобки")

    def test_mismatched_brackets(self):
        self.assertEqual(repair_brackets('(]'), '', "Должен удалить несоответствующие скобки")
        self.assertEqual(repair_brackets('[)'), '', "Должен удалить несоответствующие скобки")

    def test_mixed_unbalanced_brackets(self):
        self.assertEqual(repair_brackets('(a[b{c}d]e)'), '(a[b{c}d]e)', "Должен обрабатывать смешанные типы скобок")
        self.assertEqual(repair_brackets('(a[b{c}d]e'), 'a[b{c}d]e', "Должен удалить несоответствующую открывающую скобку")
        self.assertEqual(repair_brackets('a[b{c}d]e)'), 'a[b{c}d]e', "Должен удалить несоответствующую закрывающую скобку")

    def test_complex_case(self):
        self.assertEqual(repair_brackets('abc(d)e]f}'), 'abc(d)ef', "Должен удалить несоответствующие скобки и сохранить другие символы")

    def test_only_brackets(self):
        self.assertEqual(repair_brackets('[](){}'), '[](){}', "Должен вернуть ту же строку, если скобки сбалансированы")
        self.assertEqual(repair_brackets('[[[[]'), '[]', "Должен удалить несоответствующие открывающиеся скобки")

    def test_interleaved_brackets(self):
        self.assertEqual(repair_brackets('[(]{)}'), '{}', "Должен удалить минимальное количество скобок для балансировки")
        self.assertEqual(repair_brackets('({[)]}'), '{[]}', "Должен удалить все скобки, если их нельзя сбалансировать")

    def test_unbalanced_string(self):
        long_input = '(' * 10 + ')' * 5
        self.assertEqual(repair_brackets(long_input), '((((()))))', "Должен удалить несоответствующие открывающиеся скобки в длинных строках")

    def test_example_cases(self):
        self.assertEqual(repair_brackets(')((('), '', "Пример случая с несколькими несоответствующими скобками")
        self.assertEqual(repair_brackets('a(b)c)'), 'a(b)c', "Пример случая с одной лишней закрывающей скобкой")
        self.assertEqual(repair_brackets('([)]'), '[]', "Пример случая, когда минимальные удаления приводят к сбалансированным скобкам")

if __name__ == "__main__":
    unittest.main()
