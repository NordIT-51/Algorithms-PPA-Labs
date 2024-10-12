from random import randint

with (open('maxin8.txt', 'w') as f):
    f.write('1000\n')
    numlist=''
    for i in range(1000):
        first = randint(1, 1440)
        last = randint(first, 1440)
        numlist+=(str(first)+' '+str(last)+'\n')
    f.write(numlist)