from random import choice
from collections import defaultdict as dd

n = int(input('Enter number of sides of the dice:'))
l = list(range(1, n+1))

s = int(input('Enter the number of simulations to be used:'))
d = dd(int)
for _ in range(s):
    c = choice(l)
    d[c]+=1

for k in d.keys():
    d[k]=round(d[k]*100/s, 3)

print('The results of the simulation are:')
print('face probability')
for k in range(1, n+1):
    print(f'{k} {d[k]}%')

