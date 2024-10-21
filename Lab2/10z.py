import time
import psutil
import sys
sys.setrecursionlimit(99999999)


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


if __name__ == '__main__':
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
