import csv
import bz2
from datetime import datetime
from pprint import pprint
src = '/Users/ishan/desktop/llc/data_ingestion_with_python/resources/ch02/02_01/taxi.csv.bz2'

rownames = ['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'tip_amount', 'total_amount']
types = [int, lambda time:datetime.strptime(time, '%Y-%m-%d %H:%M:%S'), lambda time: datetime.strptime(time, '%Y-%m-%d %H:%M:%S'), int, float, float, float]



#'rt' -> read text
with bz2.open(src,'rt') as f:
    reader = csv.DictReader(f)
    record = {}
    for j, row in enumerate(reader):
        for i in range(len(types)):
            record[rownames[i]] = types[i](row[rownames[i]])
        pprint(record)
        if j>=10:
            break



