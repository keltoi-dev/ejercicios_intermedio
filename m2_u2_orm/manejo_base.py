# Practicando POO
# Germán Fraga

# import sqlite3
import os
from peewee import *

ruta = os.getcwd() + os.sep + "src" + os.sep
db = SqliteDatabase(ruta + "nomina_database.db")


# ***** FUNCIONES PARA MANEJO DE LA BASE DE DATOS *****


class BaseModel(Model):
    class Meta:
        database = db


class Empleados(BaseModel):
    dni = IntegerField(unique=True)
    cuil = IntegerField()
    nombres = CharField()
    apellidos = CharField()
    domicilio = CharField()
    f_nacimiento = CharField()
    f_alta = CharField()
    obra = CharField()
    art = CharField()
    jornal = FloatField()


# ----- CONEXION CON LA BASE DE DATOS -----
db.connect()
# ----- CREACION DE LA TABLA DE LA BASE DE DATOS -----
db.create_tables([Empleados])


class ManageBase:
    def __init__(self):
        self.empleados = Empleados()

    # ----- CONULTA A LA BASE DE DATOS -----
    def update_table(self) -> list:
        return self.empleados.select()

    def search_one(self, data):
        self.data = data
        self.data_list = []
        items = Empleados.get(Empleados.dni == self.data)
        self.data_list = [
            items.id,
            items.dni,
            items.cuil,
            items.nombres,
            items.apellidos,
            items.domicilio,
            items.f_nacimiento,
            items.f_alta,
            items.obra,
            items.art,
            items.jornal,
        ]
        return [self.data_list]

    # ----- MODIFICACION DE LA BASE DE DATOS -----
    def save_row(self, data: list):
        self.data = data
        self.empleados.dni = self.data[0]
        self.empleados.cuil = self.data[1]
        self.empleados.nombres = self.data[2]
        self.empleados.apellidos = self.data[3]
        self.empleados.domicilio = self.data[4]
        self.empleados.f_nacimiento = self.data[5]
        self.empleados.f_alta = self.data[6]
        self.empleados.obra = self.data[7]
        self.empleados.art = self.data[8]
        self.empleados.jornal = self.data[9]
        self.empleados.save()

    def delete_row(self, data):
        self.data = data
        self.borrar = Empleados.get(Empleados.dni == self.data)
        self.borrar.delete_instance()

    def modify_row(self, data):
        self.data = data
        actualizar = Empleados.update(
            nombres=self.data[3],
            apellidos=self.data[4],
            domicilio=self.data[5],
            f_nacimiento=self.data[6],
            f_alta=self.data[7],
            obra=self.data[8],
            art=self.data[9],
            jornal=self.data[10],
        ).where(Empleados.dni == self.data[0])
        actualizar.execute()

    # def modify_table(self, sql: str, data: list):
    #     self.sql = sql
    #     self.data = data
    #     self.cursor = self.conexion.cursor()
    #     self.cursor.execute(self.sql, self.data)
    #     self.conexion.commit()

    # def close_base(self):
    #     self.cursor.close()
    #     self.conexion.close()
