import time
import psutil


def longest_common_substring(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0
    end_pos_s = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos_s = i

    start_pos_s = end_pos_s - max_length
    start_pos_t = -1
    for j in range(n):
        if s[start_pos_s:start_pos_s + max_length] == t[j:j + max_length]:
            start_pos_t = j
            break

    return s[start_pos_s:end_pos_s], start_pos_s, start_pos_t, max_length


def main():
    with open('input7.txt', 'r') as file:
        lines = file.readlines()

    results = []
    for line in lines:
        s, t = line.split()
        substring, start_s, start_t, length = longest_common_substring(s, t)
        results.append(f"{start_s} {start_t} {length}")

    with open('output7.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')


if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

