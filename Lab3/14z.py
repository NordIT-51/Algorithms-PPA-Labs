import heapq
import time
import psutil


def find_min_travel_time(n, d, v, trips):
    INF = float('inf')
    graph = {i: [] for i in range(1, n + 1)}
    for from_village, start_time, to_village, end_time in trips:
        graph[from_village].append((start_time, to_village, end_time))
    min_time = {i: INF for i in range(1, n + 1)}
    min_time[d] = 0
    heap = [(0, d)]
    while heap:
        current_time, u = heapq.heappop(heap)
        if u == v:
            return current_time
        if current_time > min_time[u]:
            continue

        for start, to_village, end in graph[u]:
            if current_time <= start:
                new_time = end
                if new_time < min_time[to_village]:
                    min_time[to_village] = new_time
                    heapq.heappush(heap, (new_time, to_village))
    return -1 if min_time[v] == INF else min_time[v]


def main():
    with open('input14.txt', 'r') as fin:
        n = int(fin.readline())
        d, v = map(int, fin.readline().split())
        r = int(fin.readline())
        trips = []
        for _ in range(r):
            from_village, start_time, to_village, end_time = map(int, fin.readline().split())
            trips.append((from_village, start_time, to_village, end_time))

    result = find_min_travel_time(n, d, v, trips)
    with open('output14.txt', 'w') as fout:
        fout.write(str(result))


if __name__ == '__main__':
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
