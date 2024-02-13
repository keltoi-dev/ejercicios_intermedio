import sqlite3


# CONEXION CON LA BASE
class DataBase:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        if self.tipo == "SQLite3":
            self.conexion = sqlite3.connect(self.nombre + ".db")


class BaseDatos(DataBase):

    def __init__(self, conexion):
        super(BaseDatos, self).__init__(conexion)

    def hacer_tabla(self):
        self.cursor = self.conexion.cursor()
        sql = "CREATE TABLE compras(id integer PRIMARY KEY AUTOINCREMENT, \
        producto VARCHAR(20) NOT NULL, cantidad FLOAT, precio FLOAT)"
        self.cursor.execute(sql)
        self.conexion.commit()

    def consulta_base(self, sql, datos=""):
        self.sql = sql
        self.datos = datos
        self.cursor = self.conexion.cursor()
        if not datos:
            self.cursor.execute(self.sql)
        else:
            self.cursor.execute(self.sql, self.datos)
        self.la_lista = self.cursor.fetchall()
        return self.la_lista

    def guardar_base(self, sql, datos):
        self.sql = sql
        self.datos = datos
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.sql, self.datos)
        self.conexion.commit()
