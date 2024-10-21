import time
import psutil

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

if __name__ == '__main__':               
    t_start = time.perf_counter()
    main('input3.txt', 'output3.txt')
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
