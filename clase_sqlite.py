import sqlite3
import os

class Database:
    def __init__(self, base, *args) -> None:
        """ Params: Nombre de la base de datos y nombres de los atributos """
        self.base = base
        conn = sqlite3.connect(f"{base}.db")
        try:
            conn.execute(f"create table {base} {args}")
            print(f"Se creó la tabla {base}")                        

        except sqlite3.OperationalError:
            pass
        conn.close()

    def insert(self, *args):
        conn = sqlite3.connect(f"{self.base}.db")

        conn.execute(f"INSERT INTO {self.base} \
        VALUES {args}")

        conn.commit()
        conn.close()

    def select(self):
        conn = sqlite3.connect(f"{self.base}.db")

        conn.execute(f"SELECT * FROM {self.base}")

        conn.commit()
        conn.close()


def crearBD():
    input("Enter para volver al Menú")

def insertar():
    input("Enter para volver al Menú")

def listar():
    input("Enter para volver al Menú")

def modificar():
    input("Enter para volver al Menú")

def borrar():
    input("Enter para volver al Menú")

def main():
    op = ""
    while op != "0":
        os.system("clear")
        print("\n\nMenú de Operaciones sobre Base de Datos\n\n")
        print("1) Crear Base de Datos")
        print("2) Insertar datos")
        print("3) Listar datos")
        print("4) Modificar datos")
        print("5) Borrar datos")
        print("0) Salir")

        op = input("Ingrese opción: ")

        match op:
            case "1": crearBD()
            case "2": insertar()
            case "3": listar()
            case "4": modificar()
            case "5": borrar()

    alumnos = Database("alumno", "nombre", "fecha_nac")
    alumnos.insert("Pedro", "2001-02-02")
    alumnos.select()

if __name__ == '__main__':
    main()