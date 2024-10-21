import random


N = 10**5
max_value = 10**9
operations = ["insert", "delete", "exists", "next", "prev"]

def generate_operations(n):
    return [f"{random.choice(operations)} {random.randint(-max_value, max_value)}" for _ in range(n)]
operations_list = generate_operations(N)
with open("maxinput11.txt", "w") as file:
    for op in operations_list:
        file.write(op + "\n")
