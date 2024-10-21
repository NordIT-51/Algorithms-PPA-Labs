import unittest


def check_for_balance(node, tree, heights, balances):
    if node == -1:
        return 0
    left_descendant = tree[node][1]
    right_descendant = tree[node][2]
    left_height = check_for_balance(left_descendant, tree, heights, balances)
    right_height = check_for_balance(right_descendant, tree, heights, balances)
    height = max(left_height, right_height) + 1
    heights[node] = height
    balance = right_height - left_height
    balances[node] = balance
    return height


class TestAVLBalance(unittest.TestCase):
    def test_empty_tree(self):
        """Тест пустого дерева."""
        tree = []
        heights = []
        balances = []
        if len(tree) > 0:
            check_for_balance(0, tree, heights, balances)
        self.assertEqual(balances, [])

    def test_single_node(self):
        """Тест дерева с одним узлом."""
        tree = [(10, -1, -1)]
        heights = [0]
        balances = [0]
        check_for_balance(0, tree, heights, balances)
        self.assertEqual(heights, [1])
        self.assertEqual(balances, [0])

    def test_balanced_tree(self):
        """Тест сбалансированного дерева."""
        tree = [
            (2, 1, 2),
            (1, -1, -1),
            (3, -1, -1)
        ]
        heights = [0] * 3
        balances = [0] * 3
        check_for_balance(0, tree, heights, balances)
        self.assertEqual(heights, [2, 1, 1])
        self.assertEqual(balances, [0, 0, 0])

    def test_unbalanced_tree(self):
        """Тест несбалансированного дерева."""
        tree = [
            (1, -1, 1),
            (2, -1, 2),
            (3, -1, -1)
        ]
        heights = [0] * 3
        balances = [0] * 3
        check_for_balance(0, tree, heights, balances)
        self.assertEqual(heights, [3, 2, 1])
        self.assertEqual(balances, [2, 1, 0])

    def test_complex_tree(self):
        """Тест сложного дерева."""
        tree = [
            (5, 1, 2),
            (3, 3, 4),
            (8, -1, -1),
            (1, -1, -1),
            (4, -1, -1)
        ]
        heights = [0] * 5
        balances = [0] * 5
        check_for_balance(0, tree, heights, balances)
        self.assertEqual(heights, [3, 2, 1, 1, 1])
        self.assertEqual(balances, [-1, 0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()
