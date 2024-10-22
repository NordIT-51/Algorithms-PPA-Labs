import psutil
import time
from collections import defaultdict


def count_palindromes(s):
    position_map = defaultdict(list)
    for idx, ch in enumerate(s):
        position_map[ch].append(idx)

    total_count = 0
    for positions in position_map.values():
        m = len(positions)
        if m < 2:
            continue
        total_pairs = m * (m - 1) // 2

        prefix_sums = [0] * m
        prefix_sums[0] = positions[0]
        for i in range(1, m):
            prefix_sums[i] = prefix_sums[i - 1] + positions[i]

        total_diff = 0
        for q in range(1, m):
            i_q = positions[q]
            total = i_q * q - prefix_sums[q - 1]
            total_diff += total

        total_c = total_diff - total_pairs
        total_count += total_c

    return total_count


def main():
    with open('input2.txt', 'r') as fin:
        line = fin.readline().strip().replace(" ", "")
    res = count_palindromes(line)
    with open('output2.txt', 'w') as fout:
        fout.write(str(res))


if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
