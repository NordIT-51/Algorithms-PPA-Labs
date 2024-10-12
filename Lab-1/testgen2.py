from random import randint

with open('maxin2.txt', 'w') as f:
    f.write('100000\n')
    f.write('400\n')
    f.write('300\n')
    stoplist=''
    stop=0
    for i in range(300):
        stop+=330
        stoplist+=(str(stop)+' ')
    f.write(stoplist)