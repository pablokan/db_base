# Configuración: Editar el nombre de la base de datos y los atributos
base = "alumnos" # Reemplazar string por el nombre de la base de datos que se quiera 
atributos = ("nombre", "fecha_nac", "comision", "nota") # Reemplazar por los atributos propios

import sqlite3

conexion=sqlite3.connect(f"{base}.db")
try:
    conexion.execute(f"create table {base} {atributos}")
    print(f"Se creó la tabla {base}")                        

except sqlite3.OperationalError:
    print(f"La tabla {base} ya existe")                    
conexion.close()
