import sqlite3

db = sqlite3.connect('rides.db', detect_types=sqlite3.PARSE_DECLTYPES)
db.row_factory = sqlite3.Row

params={
        'vendor': 'VeriFone'
        }
sql = 'SELECT *  FROM rides WHERE vendor = :vendor'

cursor = db.cursor()
cursor.execute(sql, params)

distance, count = 0, 0
for row in cursor:
    #print(list(row))
    #print(row['distance'])
    distance +=(row['distance'])
    count+=1

#print(distance, count)
avg = distance/count
print('Average distance travelled: ', avg)
