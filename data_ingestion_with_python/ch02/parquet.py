import pyarrow.parquet as pq
import pandas as pd

src = '/Users/ishan/Desktop/LLC/data_ingestion_with_python/resources/ch02/02_03/taxi.parquet'

table = pq.read_table(src)

data = table.to_pandas()

print(data.dtypes)

print(data.head())

