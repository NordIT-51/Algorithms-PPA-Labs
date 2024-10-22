import time
import psutil


def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def main():
    with open('mininput5.txt', 'r') as file:
        s = file.readline().strip()
    prefix_function = compute_prefix_function(s)
    with open('output5.txt', 'w') as file:
        file.write(' '.join(map(str, prefix_function)) + '\n')


if __name__ == '__main__':
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
