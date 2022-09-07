import sqlite3
conexion=sqlite3.connect("bd1.db")
conexion.execute("""create table if not exists articulo (
                          codigo integer primary key AUTOINCREMENT,
                          descripcion text,
                          precio real
                    )""")




registro = ('frutisha',1.10)
insert = f"insert into articulo (descripcion, precio) values {registro}"
conexion.execute(insert)
conexion.commit()
conexion.close()
