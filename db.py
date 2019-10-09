
import dbm

db = dbm.open('mydb.db', 'c')
db['a'] = '1'
db['b'] = '2'
for key in db:
    print(key)
db.close()
