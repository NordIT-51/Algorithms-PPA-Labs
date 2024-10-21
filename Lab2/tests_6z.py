import unittest
import sys


sys.setrecursionlimit(19999999)
def check_tree(node, left, right, nodes):
    if node == -1:
        return True
    key, left_descendant, right_descendant = nodes[node]
    if (key <= left) or (key >= right):
        return False
    return check_tree(left_descendant, left, key, nodes) and check_tree(right_descendant, key, right, nodes)

def decide(nodes):
    if not nodes:
        return True
    return check_tree(0, float('-inf'), float('inf'), nodes)

class TestBSTChecker(unittest.TestCase):

    def test1_correct_bst(self):
        nodes = [
            (2, 1, 2),
            (1, -1, -1),
            (3, -1, -1)
        ]
        self.assertTrue(decide(nodes))

    def test2_incorrect_bst(self):
        nodes = [
            (1, 1, 2),
            (2, -1, -1),
            (3, -1, -1)
        ]
        self.assertFalse(decide(nodes))

    def test3_empty_tree(self):
        nodes = []
        self.assertTrue(decide(nodes))

    def test4_single_node(self):
        nodes = [
            (1, -1, -1)
        ]
        self.assertTrue(decide(nodes))

    def test5_duplicate_keys(self):
        nodes = [
            (2, 1, 2),
            (2, -1, -1),
            (3, -1, -1)
        ]
        self.assertFalse(decide(nodes))

    def test6_left_child_greater_than_root(self):
        nodes = [
            (2, 1, -1),
            (3, -1, -1)
        ]
        self.assertFalse(decide(nodes))

    def test7_right_child_less_than_root(self):
        nodes = [
            (2, -1, 1),
            (1, -1, -1)
        ]
        self.assertFalse(decide(nodes))

    def test8_correct_bst_large(self):
        nodes = [
            (4, 1, 2),
            (2, 3, 4),
            (6, 5, 6),
            (1, -1, -1),
            (3, -1, -1),
            (5, -1, -1),
            (7, -1, -1)
        ]
        self.assertTrue(decide(nodes))

    def test9_negative_values(self):
        nodes = [
            (-1, 1, 2),
            (-2, -1, -1),
            (0, -1, -1)
        ]
        self.assertTrue(decide(nodes))

    def test10_invalid_right_subtree(self):
        nodes = [
            (10, 1, 2),
            (5, 3, 4),
            (15, -1, -1),
            (2, -1, -1),
            (5, -1, -1)
        ]
        self.assertFalse(decide(nodes))

    def test11_max_min_values(self):
        nodes = [
            (0, 1, 2),
            (-2147483648, -1, -1),
            (2147483647, -1, -1)
        ]
        self.assertTrue(decide(nodes))

    def test12_left_child_equal_to_root(self):
        nodes = [
            (2, 1, -1),
            (2, -1, -1)
        ]
        self.assertFalse(decide(nodes))

    def test13_right_child_equal_to_root(self):
        nodes = [
            (2, -1, 1),
            (2, -1, -1)
        ]
        self.assertFalse(decide(nodes))

    def test14_deep_right_skewed_tree(self):
        n = 1000
        nodes = [(i, -1, i+1 if i+1 < n else -1) for i in range(n)]
        self.assertTrue(decide(nodes))

    def test15_left_skewed_tree_decreasing_keys(self):
        n = 1000
        nodes = [(n - i, i+1 if i+1 < n else -1, -1) for i in range(n)]
        self.assertTrue(decide(nodes))

    def test16_left_skewed_tree_equal_keys(self):
        nodes = [(0, i + 1 if i + 1 < 10 else -1, -1) for i in range(10)]
        self.assertFalse(decide(nodes))

    def test17_complex_tree(self):
        # Complex tree with mixed correctness
        nodes = [
            (8, 1, 2),
            (3, 3, 4),
            (10, -1, 5),
            (1, -1, -1),
            (6, -1, 6),
            (14, 7, -1),
            (7, -1, -1),
            (13, -1, -1)
        ]
        self.assertTrue(decide(nodes))

    if __name__ == '__main__':
        unittest.main()
