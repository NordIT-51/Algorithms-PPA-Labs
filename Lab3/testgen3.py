def generate_max_input(file_path):
    n = 1000  # Максимальное значение n
    m = 1000  # Максимальное значение m

    with open(file_path, 'w') as f:
        f.write(f"{n} {m}\n")
        # Генерируем m пар чисел в диапазоне от 1 до n
        for i in range(1, m + 1):
            a = i % n if i % n != 0 else n
            b = (i + 1) % n if (i + 1) % n != 0 else n
            # Избегаем петель (a != b)
            if a == b:
                b = (b + 1) % n if (b + 1) % n != 0 else n
            f.write(f"{a} {b}\n")

# Укажите путь к файлу, куда будет сохранен входной файл
generate_max_input('maxinput3.txt')
