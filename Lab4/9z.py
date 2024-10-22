import time
import psutil


def decompose(s):
    n = len(s)
    dp = [[''] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = s[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = s[i:j + 1]
            for k in range(i, j):
                combined = dp[i][k] + '+' + dp[k + 1][j]
                if len(combined) < len(dp[i][j]):
                    dp[i][j] = combined
            substr = s[i:j + 1]
            substr_len = len(substr)
            for l in range(1, substr_len // 2 + 1):
                if substr_len % l == 0:
                    times = substr_len // l
                    pattern = substr[0:l]
                    if pattern * times == substr:
                        candidate = dp[i][i + l - 1] + '*' + str(times)
                        if len(candidate) < len(dp[i][j]):
                            dp[i][j] = candidate
    return dp[0][n - 1]

t_start = time.perf_counter()
with open('mininput9.txt', 'r') as f:
    s = f.readline().strip()
optimal_representation = decompose(s)
with open('output9.txt', 'w') as f:
    f.write(optimal_representation)
t_end = time.perf_counter()
print(f"Время работы: {t_end - t_start:.8f} секунд.")
print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
