import time
import psutil


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


def main():
    with open('input6.txt', 'r') as fin:
        n = int(fin.readline().strip())
        nodes = []
        for i in range(n):
            nodes.append(tuple(map(int, fin.readline().strip().split())))
    if decide(nodes):
        result = "CORRECT"
    else:
        result = "INCORRECT"
    with open('output6.txt', 'w') as fout:
        fout.write(result)


if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()

print(f"Время работы: {t_end - t_start:.8f} секунд.")
print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

