import unittest
from collections import deque


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


class TestBfsShortestPath(unittest.TestCase):
    def test_simple_path(self):
        with open('input6.txt', 'w') as f:
            f.write('3 2\n')
            f.write('1 2\n')
            f.write('2 3\n')
            f.write('1 3\n')
        main()
        with open('output6.txt', 'r') as f:
            result = f.read().strip()
            self.assertEqual(result, '2')

    def test_no_path(self):
        with open('input6.txt', 'w') as f:
            f.write('3 1\n')
            f.write('1 2\n')
            f.write('2 3\n')
            f.write('1 3\n')
        main()
        with open('output6.txt', 'r') as f:
            result = f.read().strip()
            self.assertEqual(result, '-1')

    def test_same_node(self):
        with open('input6.txt', 'w') as f:
            f.write('3 2\n')
            f.write('1 2\n')
            f.write('2 3\n')
            f.write('2 2\n')
        main()
        with open('output6.txt', 'r') as f:
            result = f.read().strip()
            self.assertEqual(result, '0')

    def test_disconnected_graph(self):
        with open('input6.txt', 'w') as f:
            f.write('4 2\n')
            f.write('1 2\n')
            f.write('3 4\n')
            f.write('1 4\n')
        main()
        with open('output6.txt', 'r') as f:
            result = f.read().strip()
            self.assertEqual(result, '-1')

    def test_large_graph(self):
        with open('input6.txt', 'w') as f:
            f.write('6 7\n')
            f.write('1 2\n')
            f.write('1 3\n')
            f.write('2 4\n')
            f.write('3 4\n')
            f.write('4 5\n')
            f.write('5 6\n')
            f.write('2 6\n')
            f.write('1 6\n')
        main()
        with open('output6.txt', 'r') as f:
            result = f.read().strip()
            self.assertEqual(result, '2')

    def test_loop(self):
        with open('input6.txt', 'w') as f:
            f.write('5 5\n')
            f.write('1 2\n')
            f.write('2 3\n')
            f.write('3 4\n')
            f.write('4 5\n')
            f.write('5 1\n')
            f.write('1 4\n')
        main()
        with open('output6.txt', 'r') as f:
            result = f.read().strip()
            self.assertEqual(result, '2')

    def test_multiple_paths(self):
        with open('input6.txt', 'w') as f:
            f.write('5 6\n')
            f.write('1 2\n')
            f.write('1 3\n')
            f.write('2 4\n')
            f.write('3 4\n')
            f.write('2 5\n')
            f.write('5 4\n')
            f.write('1 4\n')
        main()

        with open('output6.txt', 'r') as f:
            result = f.read().strip()
            self.assertEqual(result, '2')


if __name__ == '__main__':
    unittest.main()
