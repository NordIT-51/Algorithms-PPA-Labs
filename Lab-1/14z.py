import time
import psutil


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def get_max_value(line):
    n = len(line) // 2 + 1
    min_values = [[0] * n for _ in range(n)]
    max_values = [[0] * n for _ in range(n)]
    for i in range(n):
        min_values[i][i] = int(line[2 * i])
        max_values[i][i] = int(line[2 * i])
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_val, max_val = float('inf'), float('-inf')
            for k in range(i, j):
                a = evalt(max_values[i][k], max_values[k + 1][j], line[2 * k + 1])
                b = evalt(max_values[i][k], min_values[k + 1][j], line[2 * k + 1])
                c = evalt(min_values[i][k], max_values[k + 1][j], line[2 * k + 1])
                d = evalt(min_values[i][k], min_values[k + 1][j], line[2 * k + 1])
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
            min_values[i][j] = min_val
            max_values[i][j] = max_val
    return max_values[0][n - 1]

with open("maxin14.txt") as file:
    t_start = time.perf_counter()
    line = file.readline().strip()
    result = get_max_value(line)
with open("maxout14.txt", "w") as file:
    file.write(str(result))
    t_end = time.perf_counter()
print(f"Время работы: {t_end - t_start:.8f} секунд.")
print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

