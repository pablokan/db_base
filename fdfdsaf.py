import sqlite3

conn = sqlite3.connect(f"una.db")
params = ('id' integer primary key autoincrement, 'nombre', 'edad')
# sql = '''CREATE TABLE "una" (
# 	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
# 	"nombre"	TEXT,
# 	"edad"	TEXT
# );'''




print(sql)
#conn.execute(sql)
print(f"Se creó la tabla una")
conn.close()

conn = sqlite3.connect(f"una.db")
args = ("Pedro", "21")
sql = f"INSERT INTO una(nombre, edad) VALUES {args};"
conn.execute(sql)


conn.commit()
conn.close()