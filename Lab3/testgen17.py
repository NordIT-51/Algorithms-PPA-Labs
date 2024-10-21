# Код для генерации максимально длинного файла ввода
N = 300
M = 100000

with open('maxinput17.txt', 'w') as file:
    file.write(f'{N} {M}\n')
    count = 0
    i = 1
    j = 2

    while count < M:
        file.write(f'{i} {j}\n')
        count += 1
        i += 1
        if i >= N:
            i = 1
            j += 1
            if j > N:
                j = 2  # Сбросить j, если превышено N
