import unittest
import tempfile
import os
from io import StringIO
import sys


def process(file_name):
    with open(file_name, 'r') as f:
        n = int(f.readline().strip())
        nodes = []
        for i in range(n):
            kstr, lstr, rstr = f.readline().strip().split()
            key = int(kstr)
            left = int(lstr)
            right = int(rstr)
            left = left - 1 if left != 0 else -1
            right = right - 1 if right != 0 else -1
            nodes.append((key, left, right))
    return n, nodes

def isBinsearch(nodes, index, min_key, max_key):
    if index == -1:
        return True
    key, left, right = nodes[index]
    if not (min_key < key < max_key):
        return False
    return (isBinsearch(nodes, left, min_key, key) and isBinsearch(nodes, right, key, max_key))

def main():
    n, nodes = process('input10.txt')
    if n == 0:
        result = "YES"
    else:
        result = "YES" if isBinsearch(nodes, 0, float('-inf'), float('inf')) else "NO"
    with open('output10.txt', 'w') as fout:
        fout.write(result + '\n')

class TestBinarySearchTree(unittest.TestCase):
    def test_process(self):
        test_input = """3
2 1 3
1 0 0
3 0 0
"""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_input:
            temp_input.write(test_input)
            temp_input_name = temp_input.name
        try:
            n, nodes = process(temp_input_name)
            expected_n = 3
            expected_nodes = [
                (2, 0, 2),
                (1, -1, -1),
                (3, -1, -1)
            ]
            self.assertEqual(n, expected_n)
            self.assertEqual(nodes, expected_nodes)
        finally:
            os.unlink(temp_input_name)

    def test_isBinsearch_valid(self):
        nodes = [
            (2, 1, 2),
            (1, -1, -1),
            (3, -1, -1)
        ]
        result = isBinsearch(nodes, 0, float('-inf'), float('inf'))
        self.assertTrue(result)

    def test_isBinsearch_invalid(self):
        nodes = [
            (1, 1, 2),
            (2, -1, -1),
            (3, -1, -1)
        ]
        result = isBinsearch(nodes, 0, float('-inf'), float('inf'))
        self.assertFalse(result)

    def test_main_yes(self):
        test_input = """3
2 1 3
1 0 0
3 0 0
"""
        with open('input10.txt', 'w') as f:
            f.write(test_input)
        try:
            original_stdout = sys.stdout
            sys.stdout = StringIO()
            main()
            with open('output10.txt', 'r') as f:
                output = f.read().strip()
            self.assertEqual(output, 'NO')
            execution_info = sys.stdout.getvalue()
            print(execution_info.strip())
        finally:
            sys.stdout = original_stdout
    def test_main_no(self):
        test_input = """3
1 2 3
2 0 0
3 0 0
"""
        with open('input10.txt', 'w') as f:
            f.write(test_input)
        try:
            original_stdout = sys.stdout
            sys.stdout = StringIO()
            main()
            with open('output10.txt', 'r') as f:
                output = f.read().strip()
            self.assertEqual(output, 'NO')
            execution_info = sys.stdout.getvalue()
            print(execution_info.strip())
        finally:
            sys.stdout = original_stdout

    def test_empty_tree(self):
        test_input = """0
"""
        with open('input10.txt', 'w') as f:
            f.write(test_input)
        try:
            original_stdout = sys.stdout
            sys.stdout = StringIO()
            main()
            with open('output10.txt', 'r') as f:
                output = f.read().strip()
            self.assertEqual(output, 'YES')
            execution_info = sys.stdout.getvalue()
            print(execution_info.strip())
        finally:
            sys.stdout = original_stdout

if __name__ == '__main__':
    unittest.main()
