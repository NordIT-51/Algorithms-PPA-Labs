# Минимально возможная строка. Каждая строка s и t может быть длиной 1 символ.

lines = ["a b"]

with open("mininput7.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
