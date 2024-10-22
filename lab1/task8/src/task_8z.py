import time
import psutil
from utils import readfile, writefile, analyze


def max_lectures(requests):
    requests.sort(key=lambda x: x[1])
    count = 0
    last_end = 0
    for start, end in requests:
        if start >= last_end:
            last_end = end
            count += 1
    return count

if __name__ == "__main__":
    inp = readfile()
    t_start = time.perf_counter()
    n = int(inp[0])
    result = []
    for i in range(n):
        line = inp[i+1]
        numbers = list(map(int, line.strip().split()))
        result.append(numbers)
    res = str(max_lectures(result))
    writefile(res)
    t_end = time.perf_counter()
    analyze(t_start,t_end)
