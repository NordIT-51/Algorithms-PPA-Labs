import time
import psutil
import sys
sys.setrecursionlimit(9999999)


def has_cycle(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)

    ifVisited = [False] * (n + 1)
    inStack = [False] * (n + 1)

    def dfs(node):
        ifVisited[node] = True
        inStack[node] = True
        for nextnode in graph[node]:
            if not ifVisited[nextnode]:
                if dfs(nextnode):
                    return True
            elif inStack[nextnode]:
                return True
        inStack[node] = False
        return False

    for node in range(1, n + 1):
        if not ifVisited[node]:
            if dfs(node):
                return True
    return False

def main():
    with open('maxinput3.txt', 'r') as fin:
        n, m = map(int, fin.readline().split())
        edges = [tuple(map(int, line.split())) for line in fin]
    res = 1 if has_cycle(n, edges) else 0
    with open('output3.txt', 'w') as fout:
        fout.write(f"{res}")

if __name__ == '__main__':
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")
