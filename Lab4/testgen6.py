from random import choice


with open('maxinput6.txt', 'w') as f:
    for i in range(1000000):
        f.write(choice('abcdefghijklmnopqrstuvwxyz'))