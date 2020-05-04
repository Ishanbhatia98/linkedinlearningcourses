import pandas as pd

src = '/Users/ishan/desktop/llc/data_ingestion_with_python/resources/ch02/02_01/taxi.csv.bz2'


time_cols = ['tpep_dropoff_datetime', 'tpep_pickup_datetime']

#can parse datetime objects while importing csv
data = pd.read_csv(src, parse_dates = time_cols)

print(data.dtypes)
