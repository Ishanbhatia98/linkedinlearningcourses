from random import randrange as rr
from time import perf_counter as pc

print('Press enter to start game')
input()
t = rr(1,6)
print(f'Your target time is {t} seconds.')
t1 = pc()
input()
t2 = pc()
diff = t2-t1
print(f'Elapsed time: {round(diff,3)} seconds.')
if diff==t:
    print('Perfect!')
elif diff>t:
    print(f'({round(diff-t,3)} seconds too slow)')
else:
    print(f'({round(t-diff,3)} seconds too fast)')

