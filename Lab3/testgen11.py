import random
import string

def generate_input_file(filename):
    # Максимальное число записей
    max_m = 1000
    # Максимальное количество различных веществ
    max_unique_substances = 100
    # Максимальная длина названия вещества
    max_name_length = 20

    # Генерация случайных уникальных названий веществ
    substances = set()
    while len(substances) < max_unique_substances:
        name_length = random.randint(1, max_name_length)
        name = ''.join(random.choices(string.ascii_letters, k=name_length))
        substances.add(name)
    substances = list(substances)

    # Генерация реакций
    m = max_m
    reactions = []
    for _ in range(m):
        substance1 = random.choice(substances)
        substance2 = random.choice(substances)
        reactions.append(f"{substance1} -> {substance2}")

    # Выбор начального и конечного веществ
    initial_substance = random.choice(substances)
    final_substance = random.choice(substances)

    # Запись в файл
    with open(filename, 'w') as file:
        file.write(f"{m}\n")
        for reaction in reactions:
            file.write(f"{reaction}\n")
        file.write(f"{initial_substance}\n")
        file.write(f"{final_substance}\n")

# Генерация файла "input.txt"
generate_input_file("maxinput11.txt")
