def generate_max_input():
    n = 10 ** 5

    with open('maxinput6.txt', 'w') as f:
        f.write(f"{n}\n")
        f.write(f"{2 ** 31 - 1} -1 -1\n")
        for i in range(1, n):
            Ki = 2 ** 31 - 1 - i
            Li = i - 1 if i % 2 == 1 else -1
            Ri = i - 1 if i % 2 == 0 else -1
            f.write(f"{Ki} {Li} {Ri}\n")


generate_max_input()
