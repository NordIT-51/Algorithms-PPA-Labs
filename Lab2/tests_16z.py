import unittest
import os
import time
import psutil


def binary_insert(items, k):
    low = 0
    high = len(items)
    while low < high:
        mid = (low + high) // 2
        if items[mid] < k:
            low = mid + 1
        else:
            high = mid
    items.insert(low, k)

def binary_remove(items, k):
    low = 0
    high = len(items)
    while low < high:
        mid = (low + high) // 2
        if items[mid] < k:
            low = mid + 1
        else:
            high = mid
    if low < len(items) and items[low] == k:
        items.pop(low)

def main(input_file='input16.txt', output_file='output16.txt', suppress_output=False):
    t_start = time.perf_counter()
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        n = int(fin.readline().strip())
        items = []
        for i in range(n):
            line = fin.readline().strip()
            if not line:
                continue
            command, k = map(int, line.split())

            if command == 1: # Добавление
                low = 0
                high = len(items)
                isDuplicate = False
                while low < high:
                    mid = (low + high) // 2
                    if items[mid] == k:
                        isDuplicate = True
                        break
                    elif items[mid] < k:
                        low = mid + 1
                    else:
                        high = mid
                if not isDuplicate:
                    binary_insert(items, k)
            elif command == 0: # Вывод
                if 0 < k <= len(items):
                    kth_maximum = items[-k]
                    fout.write(str(kth_maximum) + "\n")
                else:
                    fout.write("Error: Not enough items\n")
            elif command == -1: # Удаление
                binary_remove(items, k)
    if not suppress_output:
        t_end = time.perf_counter()
        print(f"Время работы: {t_end - t_start:.8f} секунд.")
        print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")


class TestMain(unittest.TestCase):
    def test_example_input(self):
        test_input = """11
+1 5
+1 3
+1 7
0 1
0 2
0 3
-1 5
+1 10
0 1
0 2
0 3
"""
        expected_output = """7
5
3
10
7
3
"""
        with open("input16.txt", "w") as f:
            f.write(test_input)
        main(suppress_output=True)
        with open("output16.txt", "r") as f:
            output = f.read()
        self.assertEqual(output.strip(), expected_output.strip())

    def test_add_duplicates(self):
        test_input = """6
+1 4
+1 4
+1 4
0 1
-1 4
0 1
"""
        expected_output = """4
Error: Not enough items"""
        with open("input16.txt", "w") as f:
            f.write(test_input)
        main(suppress_output=True)
        with open("output16.txt", "r") as f:
            output = f.read()
        self.assertEqual(output.strip(), expected_output.strip())

    def test_remove_non_existing(self):
        test_input = """6
+1 2
-1 5
+1 3
0 1
0 2
0 3
"""
        expected_output = """3
2
Error: Not enough items
"""
        with open("input16.txt", "w") as f:
            f.write(test_input)
        main(suppress_output=True)
        with open("output16.txt", "r") as f:
            output = f.read()
