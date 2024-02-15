import sqlite3
import pymongo


# CONEXION CON LA BASE
class DataBase:
    def __init__(self, nombre):
        self.nombre = nombre


class BaseDatos(DataBase):

    def __init__(self, nombre):
        super(BaseDatos, self).__init__(nombre)
        self.conexion = sqlite3.connect(self.nombre + ".db")

    def hacer_tabla(self):
        self.cursor = self.conexion.cursor()
        sql = "CREATE TABLE compras(id integer PRIMARY KEY AUTOINCREMENT, \
        producto VARCHAR(20) NOT NULL, cantidad FLOAT, precio FLOAT)"
        self.cursor.execute(sql)
        self.conexion.commit()

    def incorporar_base(self, datos):
        self.sql = "INSERT INTO compras(producto, cantidad, precio) VALUES (?, ?, ?)"
        self.datos = datos
        self.guardar_base(self.sql, self.datos)

    def borrar_base(self, datos):
        self.sql = "DELETE FROM compras WHERE id = ?;"
        self.datos = datos
        self.guardar_base(self.sql, self.datos)

    def modificar_base(self, datos):
        self.sql = (
            "UPDATE compras SET producto = ?, cantidad = ?, precio = ? WHERE id = ?;"
        )
        self.datos = datos
        self.guardar_base(self.sql, self.datos)

    def consulta_uno(self, datos):
        self.sql = "SELECT * FROM compras WHERE id = ?;"
        self.datos = datos
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.sql, self.datos)
        self.la_lista = self.cursor.fetchall()
        return self.la_lista

    def consulta_todo(self):
        self.sql = "SELECT * FROM compras ORDER BY id DESC;"
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.sql)
        self.la_lista = self.cursor.fetchall()
        return self.la_lista

    def guardar_base(self, sql, datos):
        self.sql = sql
        self.datos = datos
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.sql, self.datos)
        self.conexion.commit()


class Mongo(DataBase):

    def __init__(self, nombre):
        super(Mongo, self).__init__(nombre)
        client = pymongo.MongoClient("localhost", 27017)
        self.base = client[self.nombre]

    def hacer_tabla(self):
        self.coleccion = self.base["compras"]

    def incorporar_base(self, datos):
        self.datos = datos
        self.el_dict = {"producto": datos[0], "cantidad": datos[1], "precio": datos[2]}
        self.coleccion.insert_one(self.el_dict)

    def borrar_base(self, datos):
        self.datos = datos
        self.coleccion.delete_one({"producto": self.datos})

    def modificar_base(self, datos):
        self.datos = datos
        self.coleccion.update_one(
            {"producto": self.datos[3]},
            {"$set": {"producto": datos[0], "cantidad": datos[1], "precio": datos[2]}},
        )

    def consulta_uno(self, datos):
        self.datos = datos
        self.registro = self.coleccion.find_one({"producto": self.datos})
        return [list(self.registro.values())]

    def consulta_todo(self):
        self.lista = []
        for x in self.coleccion.find({}):
            self.lista.append(list(x.values()))
        return self.lista
