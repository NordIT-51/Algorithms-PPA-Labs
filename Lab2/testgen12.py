def generate_max_input_file(filename):
    N = 200000
    max_key = 10 ** 9

    with open(filename, 'w') as f:
        f.write(f"{N}\n")
        for i in range(1, N + 1):
            key = i
            left = 0
            right = i + 1 if i < N else 0
            f.write(f"{key} {left} {right}\n")


generate_max_input_file('maxinput12.txt')
