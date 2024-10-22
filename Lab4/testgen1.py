# Генерация минимально длинного файла ввода
with open('mininput1.txt', 'w') as f:
    f.write('a\n')
    f.write('a\n')

# Генерация максимально длинного файла ввода
max_length = 10**4
long_string = 'a' * max_length

with open('maxinput1.txt', 'w') as f:
    f.write(f"{long_string}\n")
    f.write(f"{long_string}\n")
