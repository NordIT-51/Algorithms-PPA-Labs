import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task_14z import evalt, get_max_value

class TestGetMaximumValue(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(get_max_value('5'), 5)

    def test_simple_addition(self):
        self.assertEqual(get_max_value('1+2'), 3)

    def test_simple_subtraction(self):
        self.assertEqual(get_max_value('5-3'), 2)

    def test_simple_multiplication(self):
        self.assertEqual(get_max_value('2*3'), 6)

    def test_mixed_operations_1(self):
        self.assertEqual(get_max_value('1+2*3'), 9)  # (1+2)*3=9

    def test_mixed_operations_2(self):
        self.assertEqual(get_max_value('2*3+4'), 14)  # 2*(3+4)=14

    def test_expression_1(self):
        self.assertEqual(get_max_value('1+5'), 6)

    def test_expression_2(self):
        self.assertEqual(get_max_value('5-8+7*4-8+9'), 200)

    def test_expression_3(self):
        self.assertEqual(get_max_value('1+2+3+4+5'), 15)

    def test_expression_4(self):
        self.assertEqual(get_max_value('1*2*3*4*5'), 120)

    def test_expression_5(self):
        self.assertEqual(get_max_value('1+2*3-4'), 5)

    def test_expression_with_zero(self):
        self.assertEqual(get_max_value('0*1+2'), 2)

    def test_negative_results(self):
        self.assertEqual(get_max_value('1-2-3'), 2)  # 1-(2-3)=2

    def test_all_operators(self):
        self.assertEqual(get_max_value('2+3*2-1'), 9)  # (2+3)*(2)-1=9

if __name__ == '__main__':
    unittest.main()
