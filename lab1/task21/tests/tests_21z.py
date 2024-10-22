import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task_21z import main

class TestMain(unittest.TestCase):

    def prepare_input(self, input_data):
        with open('input.txt', 'w') as f:
            f.write(input_data)

    def read_output(self):
        with open('output.txt', 'r') as f:
            return f.read()

    def test_sample_input(self):
        input_data = '6 2 C\nKD KC AD 7C AH 9C\n6D 6C\n'
        expected_output = 'YES'
        self.prepare_input(input_data)
        main()
        output = self.read_output()
        self.assertEqual(output, expected_output)

    def test_defense_with_trump(self):
        input_data = '5 3 S\n6S 7S 8S 9S TS\n6C 8C 9C\n'
        expected_output = 'YES'
        self.prepare_input(input_data)
        main()
        output = self.read_output()
        self.assertEqual(output, expected_output)

    def test_attacking_trump_cannot_defend(self):
        input_data = '2 1 D\n6D 7D\n8D\n'
        expected_output = 'NO'
        self.prepare_input(input_data)
        main()
        output = self.read_output()
        self.assertEqual(output, expected_output)

    def test_no_card_to_cover(self):
        input_data = '4 1 H\n6D 7D 8D 9D\n6H\n'
        expected_output = 'NO'
        self.prepare_input(input_data)
        main()
        output = self.read_output()
        self.assertEqual(output, expected_output)

    def test_cover_with_higher_same_suit(self):
        input_data = '4 1 C\n7C 8D 9H TH\n6C\n'
        expected_output = 'YES'
        self.prepare_input(input_data)
        main()
        output = self.read_output()
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
