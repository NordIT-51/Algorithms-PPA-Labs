# Генерация максимального файла ввода

# Ограничения на суммарные длины строк
max_total_t_length = 200000
max_total_p_length = 100000

# Выберем количество строк (можно изменять в зависимости от условий)
N = 1000  # Например, 1000 строк

# Вычисляем длины строк t и p для каждой строки
t_length_per_line = max_total_t_length // N
p_length_per_line = max_total_p_length // N

# Учтём остаток символов при делении
t_remainder = max_total_t_length % N
p_remainder = max_total_p_length % N

lines = []
for i in range(N):
    k = 5  # Максимально возможное значение k (если не указано иное)

    # Добавляем по одному символу к строкам t и p, пока есть остаток
    current_t_length = t_length_per_line + (1 if i < t_remainder else 0)
    current_p_length = p_length_per_line + (1 if i < p_remainder else 0)

    t = "a" * current_t_length
    p = "b" * current_p_length

    lines.append(f"{k} {t} {p}")

# Записываем в файл
with open("maxinput8.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
