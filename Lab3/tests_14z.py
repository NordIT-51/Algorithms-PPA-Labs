import unittest
import heapq


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


class TestFindMinTravelTime(unittest.TestCase):
    def test_direct_route(self):
        n = 2
        d = 1
        v = 2
        trips = [(1, 0, 2, 10)]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 10)

    def test_no_routes(self):
        n = 2
        d = 1
        v = 2
        trips = []
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, -1)

    def test_multiple_paths(self):
        n = 3
        d = 1
        v = 3
        trips = [
            (1, 0, 2, 5),
            (2, 6, 3, 10),
            (1, 0, 3, 15)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 10)

    def test_time_conflict(self):
        n = 3
        d = 1
        v = 3
        trips = [
            (1, 0, 2, 5),
            (2, 4, 3, 8)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, -1)

    def test_cyclic_paths(self):
        n = 3
        d = 1
        v = 3
        trips = [
            (1, 0, 2, 5),
            (2, 5, 1, 6),
            (1, 6, 3, 10)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 10)

    def test_immediate_departure(self):
        n = 2
        d = 1
        v = 2
        trips = [(1, 10, 2, 20)]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 20)

    def test_multiple_buses_earlier_arrival(self):
        n = 2
        d = 1
        v = 2
        trips = [
            (1, 5, 2, 15),
            (1, 10, 2, 12)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 12)

    def test_wait_for_bus(self):
        n = 2
        d = 1
        v = 2
        trips = [
            (1, 5, 2, 15)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 15)

    def test_no_need_to_wait(self):
        n = 2
        d = 1
        v = 2
        trips = [
            (1, 0, 2, 10),
            (1, 5, 2, 7)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 7)

    def test_longer_route_faster(self):
        n = 4
        d = 1
        v = 4
        trips = [
            (1, 0, 2, 10),
            (2, 15, 4, 20),
            (1, 0, 3, 5),
            (3, 5, 4, 6)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 6)

    def test_no_start_at_d(self):
        n = 2
        d = 1
        v = 2
        trips = [
            (2, 0, 1, 10)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, -1)

    def test_self_loop(self):
        n = 2
        d = 1
        v = 2
        trips = [
            (1, 0, 1, 5),
            (1, 5, 2, 10)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 10)

    def test_large_numbers(self):
        n = 2
        d = 1
        v = 2
        trips = [
            (1, 0, 2, 10000)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 10000)

    def test_multiple_routes_to_same_village(self):
        n = 3
        d = 1
        v = 3
        trips = [
            (1, 0, 2, 5),
            (1, 0, 2, 3),
            (2, 3, 3, 6),
            (2, 5, 3, 10)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 6)

    def test_long_wait(self):
        n = 3
        d = 1
        v = 3
        trips = [
            (1, 0, 2, 5),
            (2, 100, 3, 105)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 105)

    def test_start_after_time_zero(self):
        n = 3
        d = 1
        v = 3
        trips = [
            (1, 5, 2, 10),
            (2, 10, 3, 15)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 15)

    def test_same_start_and_end(self):
        n = 1
        d = 1
        v = 1
        trips = []
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 0)

    def test_bus_departed_already(self):
        n = 2
        d = 1
        v = 2
        trips = [
            (1, -1, 2, 5),
            (1, 10, 2, 15)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 15)

    def test_negative_times(self):
        n = 2
        d = 1
        v = 2
        trips = [
            (1, -5, 2, -1)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, -1)

    def test_multiple_options_same_time(self):
        n = 3
        d = 1
        v = 3
        trips = [
            (1, 0, 2, 5),
            (2, 5, 3, 10),
            (1, 0, 3, 10)
        ]
        result = find_min_travel_time(n, d, v, trips)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
