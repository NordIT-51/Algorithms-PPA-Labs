import unittest


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


class TestCalculateRefuels(unittest.TestCase):
    def test1(self):
        # Пример 1:
        d = 950
        m = 400
        stops = [200, 375, 550, 750]
        expected = 2
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test2(self):
        # Пример 2:
        d = 10
        m = 3
        stops = [1, 2, 5, 9]
        expected = -1
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test3(self):
        # Пример 3:
        d = 200
        m = 250
        stops = [100, 150]
        expected = 0
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")


    def test_impossible1(self):
        # Случай, когда невозможно добраться до первой заправки
        d = 500
        m = 100
        stops = [150, 300, 450]
        expected = -1
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test_impossible2(self):
        # Случай, когда остановки расположены через расстояние равное запасу хода
        d = 600
        m = 200
        stops = [200, 400]
        expected = 2
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test_many_stops(self):
        # Случай, когда есть лишние остановки
        d = 700
        m = 300
        stops = [100, 150, 300, 350, 500, 600, 650]
        expected = 2
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test_no_stops1(self):
        # Тестируем случай, когда заправки не нужны
        d = 500
        m = 600
        stops = []
        expected = 0
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test_no_stops2(self):
        # Тестируем случай, когда нет остановок и запас хода меньше расстояния
        d = 500
        m = 300
        stops = []
        expected = -1
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test_zero_distance(self):
        # Нулевое расстояние
        d = 0
        m = 100
        stops = []
        expected = 0
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test_zero_capacity(self):
        # Нулевая ёмкость
        d = 100
        m = 0
        stops = [50]
        expected = -1
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test_large2(self):
        # Просто большие значения
        d = 100000
        m = 10000
        stops = list(range(10000, 100000, 10000))
        expected = 9
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

    def test_large2(self):
        # Превышающие границы значения
        d = 100000
        m = 10000
        stops = list(range(10000, 100000, 10000))
        expected = 9
        result = calculate_refuels(d, m, stops.copy())
        self.assertEqual(result, expected, f"Ожидалось {expected}, получено {result}")

if __name__ == '__main__':
    unittest.main()
