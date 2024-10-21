import unittest
import sys
sys.setrecursionlimit(9999999)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._minValueNode(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def exists(self, key):
        return self._exists(self.root, key)

    def _exists(self, node, key):
        if node is None:
            return False
        if key == node.val:
            return True
        elif key < node.val:
            return self._exists(node.left, key)
        else:
            return self._exists(node.right, key)

    def next(self, key):
        succ = None
        current = self.root
        while current:
            if current.val > key:
                succ = current.val
                current = current.left
            else:
                current = current.right
        return succ

    def prev(self, key):
        pred = None
        current = self.root
        while current:
            if current.val < key:
                pred = current.val
                current = current.right
            else:
                current = current.left
        return pred

def main():
    import sys
    bst = BST()
    output = []
    with open('input5.txt', 'r') as f:
        for line in f:
            parts = line.split()
            command = parts[0]
            if command in {"insert", "delete", "exists", "next", "prev"}:
                x = int(parts[1])
                if command == "insert":
                    bst.insert(x)
                elif command == "delete":
                    bst.delete(x)
                elif command == "exists":
                    result = bst.exists(x)
                    output.append("true" if result else "false")
                elif command == "next":
                    result = bst.next(x)
                    output.append(str(result) if result is not None else "none")
                elif command == "prev":
                    result = bst.prev(x)
                    output.append(str(result) if result is not None else "none")

    with open('output5.txt', 'w') as f:
        for line in output:
            f.write(line + "\n")


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_insert_and_exists(self):
        # Тестируем вставку и проверку существования элементов
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertTrue(self.bst.exists(10))
        self.assertTrue(self.bst.exists(5))
        self.assertTrue(self.bst.exists(15))
        self.assertFalse(self.bst.exists(8))

    def test_insert_duplicates(self):
        # Тестируем вставку дубликатов
        self.bst.insert(10)
        self.bst.insert(10)
        self.bst.insert(10)
        self.bst.delete(10)
        self.assertFalse(self.bst.exists(10))

    def test_delete_leaf_node(self):
        # Тестируем удаление листового узла
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.delete(5)
        self.assertFalse(self.bst.exists(5))
        self.assertTrue(self.bst.exists(10))

    def test_delete_node_with_one_child(self):
        # Тестируем удаление узла с одним дочерним элементом
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.delete(5)
        self.assertFalse(self.bst.exists(5))
        self.assertTrue(self.bst.exists(3))
        self.assertTrue(self.bst.exists(10))

    def test_delete_node_with_two_children(self):
        # Тестируем удаление узла с двумя дочерними элементами
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(12)
        self.bst.insert(18)
        self.bst.delete(15)
        self.assertFalse(self.bst.exists(15))
        self.assertTrue(self.bst.exists(12))
        self.assertTrue(self.bst.exists(18))

    def test_next_method(self):
        # Тестируем метод next
        self.bst.insert(20)
        self.bst.insert(10)
        self.bst.insert(30)
        self.bst.insert(25)
        self.bst.insert(35)
        self.assertEqual(self.bst.next(20), 25)
        self.assertEqual(self.bst.next(25), 30)
        self.assertEqual(self.bst.next(35), None)
        self.assertEqual(self.bst.next(5), 10)

    def test_prev_method(self):
        # Тестируем метод prev
        self.bst.insert(20)
        self.bst.insert(10)
        self.bst.insert(30)
        self.bst.insert(25)
        self.bst.insert(35)
        self.assertEqual(self.bst.prev(30), 25)
        self.assertEqual(self.bst.prev(25), 20)
        self.assertEqual(self.bst.prev(10), None)
        self.assertEqual(self.bst.prev(40), 35)

    def test_all_methods_combined(self):
        # Комплексный тест всех методов
        commands = [
            ("insert", 20),
            ("insert", 10),
            ("insert", 30),
            ("insert", 25),
            ("insert", 35),
            ("delete", 20),
            ("exists", 20),
            ("exists", 25),
            ("next", 25),
            ("prev", 25),
            ("delete", 30),
            ("next", 25),
            ("prev", 25),
        ]
        expected_results = [
            None, None, None, None, None,
            None, False, True, 30, 10,
            None, 35, 10
        ]
        results = []
        for command, value in commands:
            if command == "insert":
                self.bst.insert(value)
                results.append(None)
            elif command == "delete":
                self.bst.delete(value)
                results.append(None)
            elif command == "exists":
                result = self.bst.exists(value)
                results.append(result)
            elif command == "next":
                result = self.bst.next(value)
                results.append(result)
            elif command == "prev":
                result = self.bst.prev(value)
                results.append(result)
        self.assertEqual(results, expected_results)

    def test_empty_tree(self):
        # Тестируем методы на пустом дереве
        self.assertFalse(self.bst.exists(10))
        self.assertIsNone(self.bst.next(10))
        self.assertIsNone(self.bst.prev(10))
        self.bst.delete(10)

    def test_nonexistent_delete(self):
        # Тестируем удаление несуществующего элемента
        self.bst.insert(10)
        self.bst.delete(20)
        self.assertTrue(self.bst.exists(10))

    def test_large_insert_and_delete(self):
        # Тестируем вставку и удаление большого количества элементов
        elements = list(range(1000))
        for elem in elements:
            self.bst.insert(elem)
        for elem in elements:
            self.assertTrue(self.bst.exists(elem))
        for elem in elements:
            self.bst.delete(elem)
        for elem in elements:
            self.assertFalse(self.bst.exists(elem))

if __name__ == "__main__":
    unittest.main()
