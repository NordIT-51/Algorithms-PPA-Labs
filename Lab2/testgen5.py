with open('maxinput5.txt', 'w') as file:
    for i in range(1, 101):
        file.write(f"insert {i * (10**9 // 100)}\n")
    for j in range(1, 101):
        file.write(f"exists {j * (10**9 // 100)}\n")
        file.write(f"next {j * (10**9 // 100)}\n")
        file.write(f"prev {j * (10**9 // 100)}\n")
