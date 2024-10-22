import time
import psutil


def compute_z_function(s):
    n = len(s)
    if n==0:
        return [0]
    z = [0] * n
    l, r, z[0] = 0, 0, n

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z


def main():
    with open('input6.txt', 'r') as infile:
        s = infile.readline().strip()

    z = compute_z_function(s)

    with open('output6.txt', 'w') as outfile:
        outfile.write(' '.join(map(str, z[1:])))


if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

