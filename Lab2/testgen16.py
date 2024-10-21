import random


with open('maxinput16.txt', 'w') as f:
    f.write('100000\n')
    for i in range(100000):
        f.write(random.choice(['+1', '0', '-1'])+' '+str(random.randint(-10**9, 10**9))+'\n')
