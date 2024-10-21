import unittest
import os

# Предполагается, что функция do_the_Alchemy находится в том же файле или импортирована
# from alchemy_module import do_the_Alchemy

def do_the_Alchemy():
    p = []
    a = []

    def GetID(name):
        for i in range(len(p)):
            if p[i] == name:
                return i
        p.append(name)
        for row in a:
            row.append(0)
        a.append([0] * len(p))
        return len(p) - 1

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    m = int(lines[0].strip())
    for line in lines[1:m + 1]:
        src_dest = line.strip().split('->')
        src = src_dest[0].strip()
        dest = src_dest[1].strip()
        src_id = GetID(src)
        dest_id = GetID(dest)
        a[src_id][dest_id] = 1

    start = lines[m + 1].strip()
    target = lines[m + 2].strip()
    start_id = GetID(start)
    target_id = GetID(target)

    n = len(p)
    d = [0] * n
    d[start_id] = 1

    for k in range(1, n):
        for i in range(n):
            if d[i] == k:
                for j in range(n):
                    if a[i][j] == 1 and d[j] == 0:
                        d[j] = k + 1

    if d[target_id] == 0:
        result = -1
    else:
        result = d[target_id] - 1

    with open('output.txt', 'w') as file:
        file.write(f"{result}\n")

class TestDoTheAlchemy(unittest.TestCase):
    def setUp(self):
        # Подготовка: создание пустых файлов перед каждым тестом
        with open('input.txt', 'w') as f:
            pass
        if os.path.exists('output.txt'):
            os.remove('output.txt')

    def tearDown(self):
        # Очистка: удаление файлов после каждого теста
        if os.path.exists('input.txt'):
            os.remove('input.txt')
        if os.path.exists('output.txt'):
            os.remove('output.txt')

    def test_basic_case(self):
        # Тест базового случая, где путь существует
        input_data = """4
Mercury -> Sulphur
Sulphur -> Salt
Salt -> Silver
Silver -> Gold
Mercury
Gold"""
        expected_output = "4\n"
        with open('input.txt', 'w') as f:
            f.write(input_data)

        do_the_Alchemy()

        with open('output.txt', 'r') as f:
            output = f.read()
        self.assertEqual(output, expected_output)

    def test_no_path(self):
        # Тест случая, когда пути нет
        input_data = """2
Mercury -> Sulphur
Silver -> Gold
Mercury
Gold"""
        expected_output = "-1\n"
        with open('input.txt', 'w') as f:
            f.write(input_data)

        do_the_Alchemy()

        with open('output.txt', 'r') as f:
            output = f.read()
        self.assertEqual(output, expected_output)

    def test_same_start_and_target(self):
        # Тест случая, когда начальное и конечное вещества совпадают
        input_data = """3
Mercury -> Sulphur
Sulphur -> Salt
Salt -> Silver
Mercury
Mercury"""
        expected_output = "0\n"
        with open('input.txt', 'w') as f:
            f.write(input_data)

        do_the_Alchemy()

        with open('output.txt', 'r') as f:
            output = f.read()
        self.assertEqual(output, expected_output)

    def test_cycle(self):
        # Тест случая, когда в графе есть цикл
        input_data = """4
Mercury -> Sulphur
Sulphur -> Salt
Salt -> Mercury
Salt -> Silver
Mercury
Silver"""
        expected_output = "3\n"
        with open('input.txt', 'w') as f:
            f.write(input_data)

        do_the_Alchemy()

        with open('output.txt', 'r') as f:
            output = f.read()
        self.assertEqual(output, expected_output)

    def test_disconnected_graph(self):
        # Тест случая, когда граф несвязный
        input_data = """4
Mercury -> Sulphur
Silver -> Gold
Gold -> Tin
Tin -> Lead
Mercury
Lead"""
        expected_output = "-1\n"
        with open('input.txt', 'w') as f:
            f.write(input_data)

        do_the_Alchemy()

        with open('output.txt', 'r') as f:
            output = f.read()
        self.assertEqual(output, expected_output)

    def test_multiple_paths(self):
        # Тест случая с несколькими путями, где нужно найти кратчайший
        input_data = """5
            Mercury -> Sulphur
            Mercury -> Salt
            Sulphur -> Silver
            Salt -> Silver
            Silver -> Gold
            Mercury
            Gold"""
        expected_output = "3\n"
        with open('input.txt', 'w') as f:
            f.write(input_data)

        do_the_Alchemy()

        with open('output.txt', 'r') as f:
            output = f.read()
        self.assertEqual(output, expected_output)

    def test_large_input(self):
        # Тест случая с большим количеством реакций
        reactions = [f"Substance{i} -> Substance{i + 1}" for i in range(1000)]
        input_data = f"""{len(reactions)}
            {chr(10).join(reactions)}
            Substance0
            Substance1000"""
        expected_output = "1000\n"
        with open('input.txt', 'w') as f:
            f.write(input_data)

        do_the_Alchemy()

        with open('output.txt', 'r') as f:
            output = f.read()
        self.assertEqual(output, expected_output)

    if __name__ == '__main__':
        unittest.main()
