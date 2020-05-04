import sqlite3 as sql
import pandas as pd


conn = sql.connect('rides.db', detect_types = sql.PARSE_DECLTYPES)
df = pd.read_sql('SELECT * FROM rides', conn)

df['duration'] = df['dropoff']-df['pickup']
mask = df['duration'] > pd.Timedelta(1 , 'm')

df = df[mask]
median = df.duration.median()
df.loc[df.duration>pd.Timedelta(5,'h'), 'duration'] = median

print(df.shape)
print(f'max:{df.duration.max()}, min:{df.duration.min()}')

print(df.head())



