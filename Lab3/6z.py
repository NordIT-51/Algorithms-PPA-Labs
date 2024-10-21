from collections import deque
import time
import psutil


def bfs_shortest_path(graph, start, end):
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        current, distance = queue.popleft()
        if current == end:
            return distance
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            queue.append((neighbor, distance + 1))
    return -1

def main():
    with open('input6.txt', 'r') as fin:
        n, m = map(int, fin.readline().strip().split())
        graph = {i: [] for i in range(1, n + 1)}
        for i in range(m):
            a, b = map(int, fin.readline().strip().split())
            graph[a].append(b)
            graph[b].append(a)
        u, v = map(int, fin.readline().strip().split())
    result = bfs_shortest_path(graph, u, v)
    with open('output6.txt', 'w') as fout:
        fout.write(str(result))


if __name__ == '__main__':
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
