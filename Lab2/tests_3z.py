import unittest
import tempfile
import os
import sys
sys.setrecursionlimit(999999)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, x):
        self.root = self._add(self.root, x)

    def _add(self, node, x):
        if node is None:
            return Node(x)
        if x < node.key:
            node.left = self._add(node.left, x)
        elif x > node.key:
            node.right = self._add(node.right, x)
        return node

    def findmin(self, x):
        result = self._findmin(self.root, x)
        return result if result is not None else 0

    def _findmin(self, node, x):
        successor = None
        while node:
            if node.key > x:
                successor = node.key
                node = node.left
            else:
                node = node.right
        return successor

def main(input_file, output_file):
    bst = BST()
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        for line in fin:
            command = line.strip()
            if command.startswith('+'):
                _, x = command.split()
                bst.add(int(x))
            elif command.startswith('>'):
                _, x = command.split()
                result = bst.findmin(int(x))
                fout.write(f"{result}\n")

class TestBST(unittest.TestCase):
    def test_add_and_findmin(self):
        bst = BST()
        bst.add(5)
        bst.add(3)
        bst.add(9)
        self.assertEqual(bst.findmin(4), 5)
        self.assertEqual(bst.findmin(5), 9)
        self.assertEqual(bst.findmin(9), 0)
        self.assertEqual(bst.findmin(2), 3)

        bst.add(-1)
        self.assertEqual(bst.findmin(-2), -1)

        bst.add(5)
        self.assertEqual(bst.findmin(5), 9)

        empty_bst = BST()
        self.assertEqual(empty_bst.findmin(0), 0)

    def test_findmin_with_no_elements_greater(self):
        bst = BST()
        bst.add(1)
        bst.add(2)
        bst.add(3)
        self.assertEqual(bst.findmin(3), 0)

    def test_findmin_with_negative_numbers(self):
        bst = BST()
        bst.add(-10)
        bst.add(-5)
        bst.add(-1)
        self.assertEqual(bst.findmin(-6), -5)
        self.assertEqual(bst.findmin(-2), -1)
        self.assertEqual(bst.findmin(0), 0)

class TestMainFunction(unittest.TestCase):
    def test_main_function(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_input, tempfile.NamedTemporaryFile(mode='r+', delete=False) as temp_output:
            commands = [
                '+ 5',
                '+ 3',
                '+ 9',
                '> 4',
                '> 5',
                '> 9',
                '> 2'
            ]
            temp_input.write('\n'.join(commands))
            temp_input.flush()
            temp_input.close()
            temp_output.close()

            main(temp_input.name, temp_output.name)

            with open(temp_output.name, 'r') as output_file:
                outputs = output_file.read().splitlines()

            expected_outputs = ['5', '9', '0', '3']
            self.assertEqual(outputs, expected_outputs)

            os.unlink(temp_input.name)
            os.unlink(temp_output.name)

    def test_main_with_empty_input(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_input, tempfile.NamedTemporaryFile(mode='r+', delete=False) as temp_output:

            temp_input.flush()
            temp_input.close()
            temp_output.close()

            main(temp_input.name, temp_output.name)

            with open(temp_output.name, 'r') as output_file:
                outputs = output_file.read().splitlines()

            self.assertEqual(outputs, [])

            os.unlink(temp_input.name)
            os.unlink(temp_output.name)

    def test_main_with_negative_numbers(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_input, tempfile.NamedTemporaryFile(mode='r+', delete=False) as temp_output:

            commands = [
                '+ -5',
                '+ -3',
                '+ -9',
                '+ 0',
                '> -4',
                '> -9',
                '> -2',
                '> 0'
            ]
            temp_input.write('\n'.join(commands))
            temp_input.flush()
            temp_input.close()
            temp_output.close()

            main(temp_input.name, temp_output.name)

            with open(temp_output.name, 'r') as output_file:
                outputs = output_file.read().splitlines()

            expected_outputs = ['-3', '-5', '0', '0']
            self.assertEqual(outputs, expected_outputs)

            os.unlink(temp_input.name)
            os.unlink(temp_output.name)

    def test_main_with_duplicates(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_input, tempfile.NamedTemporaryFile(mode='r+', delete=False) as temp_output:

            commands = [
                '+ 5',
                '+ 5',
                '+ 5',
                '> 4',
                '> 5',
                '+ 6',
                '> 5'
            ]
            temp_input.write('\n'.join(commands))
            temp_input.flush()
            temp_input.close()
            temp_output.close()

            main(temp_input.name, temp_output.name)

            with open(temp_output.name, 'r') as output_file:
                outputs = output_file.read().splitlines()

            expected_outputs = ['5', '0', '6']
            self.assertEqual(outputs, expected_outputs)

            os.unlink(temp_input.name)
            os.unlink(temp_output.name)

    def test_main_with_large_input(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_input, tempfile.NamedTemporaryFile(mode='r+', delete=False) as temp_output:
            commands = ['+ {}'.format(i) for i in range(1000)]
            commands += ['> 500']
            temp_input.write('\n'.join(commands))
            temp_input.flush()
            temp_input.close()
            temp_output.close()

            main(temp_input.name, temp_output.name)

            with open(temp_output.name, 'r') as output_file:
                outputs = output_file.read().splitlines()

            self.assertEqual(outputs, ['501'])

            os.unlink(temp_input.name)
            os.unlink(temp_output.name)


if __name__ == '__main__':
    unittest.main()
