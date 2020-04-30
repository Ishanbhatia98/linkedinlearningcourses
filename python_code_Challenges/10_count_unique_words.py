from collections import Counter
import string

path = input('Enter path to file: ')

f = open(path, 'r')

raw_text = f.read()

#removing chars
for char in string.punctuation:
    raw_text=raw_text.replace(char, ' ')

#to lower case
raw_text=raw_text.lower()

#conversion to list
l = raw_text.split()

#word count
print('Word count:', len(l))

#intitializing counter
c = Counter(l)

#printing top 20
print('The top 20 most common words are:')
print('Word count')
for i in c.most_common(20):
    print(*i)

