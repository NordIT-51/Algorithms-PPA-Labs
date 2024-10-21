def generate_max_input_file(filename):
    n = 100000
    m = 100000
    u = 1
    v = n

    with open(filename, 'w') as file:
        file.write(f"{n} {m}\n")
        file.write(f"{u} {v}\n")
        for i in range(1, m + 1):
            x = (i % n) + 1
            y = ((i + 1) % n) + 1
            file.write(f"{x} {y}\n")


generate_max_input_file('maxinput6.txt')
