from random import randint


with open('maxin15.txt', 'w') as f:
    res = ''
    for i in range(100):
        res+=['(',')','{','}','[',']'][randint(0,5)]
    f.write(res)