import unittest


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


class TestCycleDetection(unittest.TestCase):
    def test_empty_graph(self):
        n = 5
        edges = []
        self.assertFalse(has_cycle(n, edges), "Пустой граф не должен содержать цикл")

    def test_single_edge(self):
        n = 2
        edges = [(1, 2)]
        self.assertFalse(has_cycle(n, edges), "Граф с одним ребром не должен содержать цикл")

    def test_simple_cycle(self):
        n = 2
        edges = [(1, 2), (2, 1)]
        self.assertTrue(has_cycle(n, edges), "Граф с циклом между двумя вершинами должен содержать цикл")

    def test_three_node_cycle(self):
        n = 3
        edges = [(1, 2), (2, 3), (3, 1)]
        self.assertTrue(has_cycle(n, edges), "Граф с циклом из трех вершин должен содержать цикл")

    def test_acyclic_graph(self):
        n = 4
        edges = [(1, 2), (2, 3), (3, 4)]
        self.assertFalse(has_cycle(n, edges), "Ациклический граф не должен содержать цикл")

    def test_graph_with_back_edge(self):
        n = 4
        edges = [(1, 2), (2, 3), (3, 4), (4, 2)]
        self.assertTrue(has_cycle(n, edges), "Граф с обратным ребром должен содержать цикл")

    def test_disconnected_graph(self):
        n = 6
        edges = [(1, 2), (2, 3), (3, 1), (4, 5)]
        self.assertTrue(has_cycle(n, edges), "Граф с циклом в одной из компонент должен содержать цикл")

    def test_disconnected_acyclic_graph(self):
        n = 6
        edges = [(1, 2), (3, 4), (5, 6)]
        self.assertFalse(has_cycle(n, edges), "Несвязный ациклический граф не должен содержать цикл")

    def test_self_loop(self):
        n = 3
        edges = [(1, 1), (2, 3)]
        self.assertTrue(has_cycle(n, edges), "Граф с ребром-петлей должен содержать цикл")

    def test_complex_graph(self):
        n = 6
        edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 6), (6, 4)]
        self.assertTrue(has_cycle(n, edges), "Сложный граф с несколькими циклами должен содержать цикл")


if __name__ == '__main__':
    unittest.main()
