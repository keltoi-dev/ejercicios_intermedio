# Practicando POO
# Germán Fraga

# import sqlite3
import os
from peewee import SqliteDatabase, Model
from peewee import IntegerField, CharField, FloatField

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
    def __init__(self) -> None:
        pass

    # ----- CONULTA A LA BASE DE DATOS -----
    def update_table(self) -> list:
        return Empleados.select()

    def filter_table(self, data: str):
        self.data = data
        return Empleados.select().where(Empleados.obra == self.data)

    def search_one(self, data: str) -> list:
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
    def save_row(self, data: list) -> None:
        self.data = data
        empleado = Empleados()
        empleado.dni = self.data[0]
        empleado.cuil = self.data[1]
        empleado.nombres = self.data[2]
        empleado.apellidos = self.data[3]
        empleado.domicilio = self.data[4]
        empleado.f_nacimiento = self.data[5]
        empleado.f_alta = self.data[6]
        empleado.obra = self.data[7]
        empleado.art = self.data[8]
        empleado.jornal = self.data[9]
        empleado.save()

    def delete_row(self, data: str) -> None:
        self.data = data
        self.borrar = Empleados.get(Empleados.dni == self.data)
        self.borrar.delete_instance()

    def modify_row(self, data: list) -> None:
        self.data = data
        actualizar = Empleados.update(
            nombres=self.data[2],
            apellidos=self.data[3],
            domicilio=self.data[4],
            f_nacimiento=self.data[5],
            f_alta=self.data[6],
            obra=self.data[7],
            art=self.data[8],
            jornal=self.data[9],
        ).where(Empleados.dni == self.data[0])
        actualizar.execute()
