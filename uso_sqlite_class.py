from sqlite_class import Database

dbd = {"filename": 'kan_pru_01.db', "table": 'kan_table_01'}

db = Database(**dbd)

print(f'Create table {dbd["table"]}')
db.sql_do(f'drop table if exists {dbd["table"]}')
db.sql_do(f'create table {dbd["table"]} ( t1 text, i1 int )')

print('Create rows')
db.insert(dict(t1 = 'one', i1 = 1))
db.insert(dict(t1 = 'two', i1 = 2))
db.insert(dict(t1 = 'three', i1 = 3))
db.insert(dict(t1 = 'four', i1 = 4))
for row in db: print(row)

print('Retrieve rows')
print(db.retrieve('one'), db.retrieve('two'))

print('Update rows')
db.update(dict(t1 = 'one', i1 = 101))
db.update(dict(t1 = 'three', i1 = 103))
for row in db: print(row)

print('Delete rows')
db.delete('one')
db.delete('three')
for row in db: print(row)
