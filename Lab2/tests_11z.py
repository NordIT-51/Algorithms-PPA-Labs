import unittest
import bisect


def process(operations):
    elements = []
    results = []
    for line in operations:
        op, *args = line.strip().split()
        x = int(args[0]) if args else None

        if op == 'insert':
            idx = bisect.bisect_left(elements, x)
            if idx == len(elements) or elements[idx] != x:
                elements.insert(idx, x)
        elif op == 'delete':
            idx = bisect.bisect_left(elements, x)
            if idx < len(elements) and elements[idx] == x:
                elements.pop(idx)
        elif op == 'exists':
            idx = bisect.bisect_left(elements, x)
            results.append('true' if idx < len(elements) and elements[idx] == x else 'false')
        elif op == 'next':
            idx = bisect.bisect_right(elements, x)
            results.append(str(elements[idx]) if idx < len(elements) else 'none')
        elif op == 'prev':
            idx = bisect.bisect_left(elements, x)
            if idx > 0:
                results.append(str(elements[idx - 1]))
            else:
                results.append('none')

    return results

if __name__ == '__main__':
    with open('maxinput11.txt', 'r') as fin:
        operations = fin.readlines()
        results = process(operations)
    with open('output11.txt', 'w') as fout:
        for result in results:
            fout.write(result + '\n')

class TestProcess(unittest.TestCase):
    def test_insert_and_exists(self):
        operations = [
            'insert 5',
            'exists 5',
            'exists 10',
            'insert 10',
            'exists 10'
        ]
        expected_results = ['true', 'false', 'true']
        self.assertEqual(process(operations), expected_results)

    def test_delete(self):
        operations = [
            'insert 5',
            'insert 10',
            'delete 5',
            'exists 5',
            'exists 10',
            'delete 10',
            'exists 10'
        ]
        expected_results = ['false', 'true', 'false']
        self.assertEqual(process(operations), expected_results)

    def test_next(self):
        operations = [
            'insert 5',
            'insert 10',
            'insert 15',
            'next 7',
            'next 10',
            'next 15',
            'next 20'
        ]
        expected_results = ['10', '15', 'none', 'none']
        self.assertEqual(process(operations), expected_results)

    def test_prev(self):
        operations = [
            'insert 5',
            'insert 10',
            'insert 15',
            'prev 7',
            'prev 10',
            'prev 5',
            'prev 0'
        ]
        expected_results = ['5', '5', 'none', 'none']
        self.assertEqual(process(operations), expected_results)

    def test_combined_operations(self):
        operations = [
            'insert 5',
            'insert 10',
            'insert 15',
            'delete 10',
            'exists 10',
            'next 5',
            'prev 15',
            'next 15',
            'prev 5'
        ]
        expected_results = ['false', '15', '5', 'none', 'none']
        self.assertEqual(process(operations), expected_results)

    def test_duplicate_inserts(self):
        operations = [
            'insert 5',
            'insert 5',
            'insert 5',
            'exists 5',
            'next 5',
            'prev 5',
            'delete 5',
            'exists 5'
        ]
        expected_results = ['true', 'none', 'none', 'false']
        self.assertEqual(process(operations), expected_results)

    def test_nonexistent_deletes(self):
        operations = [
            'delete 5',
            'exists 5',
            'insert 10',
            'delete 5',
            'exists 10',
            'delete 10',
            'exists 10'
        ]
        expected_results = ['false', 'true', 'false']
        self.assertEqual(process(operations), expected_results)

    def test_large_numbers(self):
        operations = [
            'insert 1000000000',
            'insert -1000000000',
            'exists 1000000000',
            'exists -1000000000',
            'prev 0',
            'next 0'
        ]
        expected_results = ['true', 'true', '-1000000000', '1000000000']
        self.assertEqual(process(operations), expected_results)

    def test_no_operations(self):
        operations = []
        expected_results = []
        self.assertEqual(process(operations), expected_results)

    def test_only_inserts(self):
        operations = [
            'insert 1',
            'insert 2',
            'insert 3',
            'insert 4',
            'insert 5'
        ]
        expected_results = []
        self.assertEqual(process(operations), expected_results)

    if __name__ == '__main__':
        unittest.main()

