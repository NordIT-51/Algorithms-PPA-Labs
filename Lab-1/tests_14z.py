import unittest

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def get_max_value(line):
    n = len(line) // 2 + 1
    min_values = [[0] * n for _ in range(n)]
    max_values = [[0] * n for _ in range(n)]

    for i in range(n):
        min_values[i][i] = int(line[2 * i])
        max_values[i][i] = int(line[2 * i])

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_val, max_val = float('inf'), float('-inf')
            for k in range(i, j):
                a = evalt(max_values[i][k], max_values[k + 1][j], line[2 * k + 1])
                b = evalt(max_values[i][k], min_values[k + 1][j], line[2 * k + 1])
                c = evalt(min_values[i][k], max_values[k + 1][j], line[2 * k + 1])
                d = evalt(min_values[i][k], min_values[k + 1][j], line[2 * k + 1])
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
            min_values[i][j] = min_val
            max_values[i][j] = max_val

    return max_values[0][n - 1]

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
