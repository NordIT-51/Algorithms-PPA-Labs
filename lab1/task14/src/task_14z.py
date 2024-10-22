import time
import psutil
from utils import readfile, writefile, analyze


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

if __name__ == "__main__":
    inp = readfile()
    t_start = time.perf_counter()
    line = inp[0].strip()
    writefile(get_max_value(line))
    t_end = time.perf_counter()
    analyze(t_start, t_end)

