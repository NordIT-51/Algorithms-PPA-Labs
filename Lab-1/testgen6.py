from random import randint

with (open('maxin6.txt', 'w') as f):
    f.write('100\n')
    numlist=''
    for i in range(100):
        numlist+=(str(randint(1,1000))+' ')
    f.write(numlist)