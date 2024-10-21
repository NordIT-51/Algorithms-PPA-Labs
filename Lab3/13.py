import time
import psutil


def find_gardens(n, m, grid):
    def dfs(x, y):
        stack = [(x, y)]
        grid[x][y] = '.'
        while stack:
            cx, cy = stack.pop()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '#':
                    grid[nx][ny] = '.'
                    stack.append((nx, ny))

    garden_count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                garden_count += 1
                dfs(i, j)

    return garden_count


def main():
    with open('input13.txt', 'r') as fin:
        lines = fin.readlines()
    n, m = map(int, lines[0].strip().split())
    grid = [list(line.strip()) for line in lines[1:]]
    result = find_gardens(n, m, grid)
    with open('output13.txt', 'w') as fout:
        fout.write(str(result))


if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")

