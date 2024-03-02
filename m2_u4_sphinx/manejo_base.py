"""
manejo_base.py:
    Controla todas las operaciones a realizar en la base de datos a través
    del ORM Peewee en SQLite3.
"""

import os
import datetime
from peewee import SqliteDatabase, Model, IntegrityError
from peewee import IntegerField, CharField, FloatField

ruta = os.getcwd() + os.sep + "src" + os.sep
db = SqliteDatabase(ruta + "nomina_database.db")


# ***** FUNCIONES PARA MANEJO DE LA BASE DE DATOS *****


class BaseModel(Model):
    class Meta:
        database = db


class Empleados(BaseModel):
    """
    Declaración de los campos de la tabla con su tipo de dato y como único el dni.
    """

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
        """
        Consulta a todos los registro contenidos en la base de datos.

        :returns: Todos la informacion de la tabla Empleados
        :rtype: list[str, int]
        """
        return Empleados.select()

    def filter_table(self, data: str):
        """
        Filtra la información por el nombre de la obra para la carga en el treeview.

        :param data: String con el dato del campo filtro
        :returns: Todos la informacion de la tabla Empleados
        :rtype: list[str, int]
        """
        self.data = data
        return Empleados.select().where(Empleados.obra == self.data)

    def search_one(self, data: str) -> list:
        """
        Carga un registro de la tabla de acuerdo al id solicitado.
        Genera una lista con toda la información recibida por el ORM.

        :param data: Número de id seleccionado
        :returns: Todos la información de la tabla Empleados
        :rtype: list[str, int]
        """

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
        """
        Graba la informacion cargada en la base de datos, previa asigancion a cada uno de los campos
        del registro desde la lista recibida.

        :param data: Lista con toda la informacion cargada
        """
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
        """
        Se elimina todo un registro de la tabla de acuerdo al número de dni recibido.

        :param data: Número de dni seleccionado
        """
        self.data = data
        self.borrar = Empleados.get(Empleados.dni == self.data)
        self.borrar.delete_instance()

    def modify_row(self, data: list) -> None:
        """
        Actualización del registro seleccionado, dejando sin posibilidad de modificación
        el campo del DNI y del CUIL.

        :param data: Lista con los datos a modificar
        """
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


class BaseError(Exception):
    """
    Clase para la generación de un propio tipo de error para el manejo de
    excepciones en el uso del ORM.
    Genera un un log con la información del error.
    """

    BASE_DIR = os.getcwd() + os.sep
    ruta = BASE_DIR + "log.txt"

    def __init__(self) -> None:
        pass

    def guardar_error(self) -> None:
        """
        Función que guarda el tipo de error, donde se localizó y la fecha y hora.
        """
        log_errors = open(self.ruta, "a")
        print(
            datetime.datetime.now(),
            "- Se intenta cargar un dni ya existente en la base en Alta",
            file=log_errors,
        )
