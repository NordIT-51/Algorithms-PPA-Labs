import time
import psutil


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
    with open('input8.txt', 'r') as fin, open('output8.txt', 'w') as fout:
        t_start = time.perf_counter()
        n = int(fin.readline())
        result = []
        for _ in range(n):
            line = fin.readline()
            numbers = list(map(int, line.strip().split()))
            result.append(numbers)
        res = str(max_lectures(result))
        fout.write(res)
        t_end = time.perf_counter()

print(f"Время работы: {t_end - t_start:.8f} секунд.")
print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

