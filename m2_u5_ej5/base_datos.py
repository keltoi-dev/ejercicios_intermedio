import sqlite3


# CONEXION CON LA BASE
class BaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("m2_u2_database.db")

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
