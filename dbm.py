import dbm


db = dbm.open("dbm.db", "n")

db['one'] = '1'
db['two'] = '2'
db['three'] = '3'


db.close()
