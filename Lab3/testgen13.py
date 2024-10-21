from random import choice


def generate_max_input_file():
    N, M = 200, 200
    with open("maxinput13.txt", "w") as file:
        file.write(f"{N} {M}\n")
        for i in range(N):
            line = ''
            for n in range(M):
                line += choice(['#', '.'])
            file.write(line + "\n")

generate_max_input_file()
