from random import choice


with open('maxinput2.txt', 'w') as f:
    for i in range(300000):
        f.write(choice('abcdefghijklmnopqrstuvwxyz '))