import time
import psutil
import sys
sys.setrecursionlimit(999999)

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


def main():
    with open('input12.txt', 'r') as fin:
        n = int(fin.readline().strip())
        tree = []

        for _ in range(n):
            k, l, r = map(int, fin.readline().strip().split())
            tree.append((k, l - 1, r - 1))

    heights = [0] * n
    balances = [0] * n

    if n > 0:
        check_for_balance(0, tree, heights, balances)

    with open("output12.txt", "w") as fout:
        for balance in balances:
            fout.write(f"{balance}\n")


if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

