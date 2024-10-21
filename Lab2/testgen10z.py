def create_max_input_file(filename='maxinput10.txt'):
    N = 200000  # максимально допустимое значение для N
    max_key = 10**9
    lines = []

    # Первая строка - число вершин
    lines.append(f"{N}\n")

    # Генерация описания для каждой вершины
    for i in range(1, N + 1):
        # Используем максимальные значения ключей
        key = max_key - i
        # Позиция левого и правого ребёнка
        left = i + 1 if i + 1 <= N else 0
        right = i + 2 if i + 2 <= N else 0
        lines.append(f"{key} {left} {right}\n")

    # Запись в файл
    with open(filename, 'w') as file:
        file.writelines(lines)

# Вызываем функцию для создания файла
create_max_input_file()
