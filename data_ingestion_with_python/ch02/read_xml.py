import pandas as pd
import bz2
import xml.etree.ElementTree as xml
from pprint import pprint 

src = '/Users/ishan/desktop/llc/data_ingestion_with_python/resources/ch02/02_02/taxi.xml.bz2'

conversions = [
                ('vendor', int),
                ('people', int),
                ('tip', float),
                ('price', float),
                ('pickup', pd.to_datetime),
                ('dropoff', pd.to_datetime),
                ('distance', float)
                ]




def readXML():
    with bz2.open(src, 'rt') as f:
        tree = xml.parse(f)

        for element in tree.getroot():
            record = {}
            for tag, func in conversions:
                record[tag] = func(element.find(tag).text)
            #pprint(record) 
            yield record

records = readXML()
data = pd.DataFrame.from_records(records)
print(data.dtypes)
print(data.head())
