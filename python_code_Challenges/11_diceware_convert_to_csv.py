import csv

f = open('diceware.txt', 'r')
lines = f.readlines()
d = dict()

#saving diceware values in a dictionary
for line in lines:
    r = line.strip().replace('\t',' ').split()
    d[r[0]] = r[1]

#writing dictionary to csv
w = csv.writer(open('diceware.csv', 'w'))
for k, v in d.items():
    w.writerow([k, v])


