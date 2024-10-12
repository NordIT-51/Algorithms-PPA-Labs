import time
import psutil


def calculate_refuels(d, m, stops):
    stops.append(d)
    refill_num = 0
    pos = 0
    reach = m
    i = 0
    while pos < d:
        if reach >= d:
            break
        last_pos = pos
        while i < len(stops) and stops[i] <= reach:
            last_pos = stops[i]
            i += 1
        if last_pos == pos:
            return -1
        refill_num += 1
        pos = last_pos
        reach = pos + m
    return refill_num


with open('input2.txt', 'r') as fin, open('output2.txt', 'w') as fout:
    t_start = time.perf_counter()
    d = int(fin.readline().strip())
    t = int(fin.readline().strip())
    n = int(fin.readline().strip())
    stops = list(map(int, fin.readline().strip().split()))
    result = calculate_refuels(d, t, stops)
    fout.write(str(result) + '\n')
    t_end = time.perf_counter()

print(f"Время работы: {t_end - t_start:.8f} секунд.")
print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")


