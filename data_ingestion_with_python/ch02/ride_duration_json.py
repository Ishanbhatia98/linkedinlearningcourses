import json
from datetime import datetime, timedelta
from pprint import pprint
import operator
from functools import reduce

src = '/Users/ishan/Desktop/LLC/data_ingestion_with_python/resources/ch02/02_05/taxi.jl'
delta = []
with open(src, 'r') as f:
    for line in f.readlines():
        d = json.loads(line)
        p = d['pickup'][:-1]
        p = p.split('T')
        p = datetime.strptime(' '.join(p),'%Y-%m-%d %H:%M:%S.%f')
        
        dr = d['dropoff'][:-1]
        dr = dr.split('T')
        dr = datetime.strptime(' '.join(dr), '%Y-%m-%d %H:%M:%S.%f')

        delta.append(dr-p)

print('Average time for a journey:', end = ' ')
print(reduce(operator.add, delta)/len(delta))

#print(sum(delta)/len(delta))
