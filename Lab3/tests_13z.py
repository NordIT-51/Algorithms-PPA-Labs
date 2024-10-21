import unittest


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


class TestCountBeds(unittest.TestCase):

    def test_example_1(self):
        grid = [
            ['#', '#', '.', '.', '.', '.', '.', '.', '#', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
        ]
        n = len(grid)
        m = len(grid[0]) if grid else 0
        self.assertEqual(find_gardens(n, m, grid), 2)

    def test_example_2(self):
        grid = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ]
        n = len(grid)
        m = len(grid[0]) if grid else 0
        self.assertEqual(find_gardens(n, m, grid), 1)

    def test_no_beds(self):
        grid = [
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]
        n = len(grid)
        m = len(grid[0]) if grid else 0
        self.assertEqual(find_gardens(n, m, grid), 0)

    def test_one_large_bed(self):
        grid = [
            ['#', '#', '#'],
            ['#', '#', '#'],
            ['#', '#', '#'],
        ]
        n = len(grid)
        m = len(grid[0]) if grid else 0
        self.assertEqual(find_gardens(n, m, grid), 1)


if __name__ == '__main__':
    unittest.main()
