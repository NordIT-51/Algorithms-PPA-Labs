from random import randint


def card():
    rank = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'][randint(0,8)]
    suit = ['S', 'C', 'D', 'H'][randint(0,3)]
    return rank + suit

with open('maxin21.txt', 'w') as f:
    f.write('35 4 ')
    f.write(['S', 'C', 'D', 'H'][randint(0,3)]+'\n')
    for i in range(35):
        f.write(card()+' ')
    f.write('\n')
    for i in range(4):
        f.write(card()+' ')