from random import randint

with open('maxin14.txt', 'w') as f:
    line = ''
    for i in range(29):
        line += (['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'][randint(0,9)])
        line += (['+', '-', '*'][randint(0,2)])
    f.write(line[:-1])
