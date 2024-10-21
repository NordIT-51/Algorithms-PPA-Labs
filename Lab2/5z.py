import time
import psutil


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

if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

