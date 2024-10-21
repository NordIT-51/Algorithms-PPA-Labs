import random

N = 300000
min_value = 1
max_value = 10**9

with open('maxinput3.txt', 'w') as f:
    for _ in range(N):
        x = random.randint(min_value, max_value)
        f.write(f"{random.choice(['+', '>'])+' '+str(x)}\n")
