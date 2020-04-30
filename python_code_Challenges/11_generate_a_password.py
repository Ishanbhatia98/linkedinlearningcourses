import csv
from random import choice

def gen_num_phrase():
    dice = list(map(str, list(range(1, 7))))
    num_phrase = []
    for _ in range(5):
        num_phrase.append(choice(dice))
    return ''.join(num_phrase)





#importing diceware dictionary

reader = csv.reader(open('11_diceware.csv'))

#crearing dictionary
d = dict()
for r in reader:
    d[r[0]]=r[1]

n = int(input('Enter number of words to be used in the passphrase: '))

#generatiing phrase

phrase = []
for _ in range(n):
    phrase.append(d[gen_num_phrase()])

print('Your passphrase: ')
print(' '.join(phrase))

