# Practicando POO
# Germán Fraga

import sqlite3
import os


# ***** FUNCIONES PARA MANEJO DE LA BASE DE DATOS *****
# ----- CONEXION CON LA BASE DE DATOS -----


class ManageBase:
    def __init__(self):
        ruta = os.getcwd() + os.sep + "src" + os.sep
        self.conexion = sqlite3.connect(ruta + "nomina_database.db")

    # ----- CREACION DE LA TABLA DE LA BASE DE DATOS -----
    def create_table(self):
        cursor = self.conexion.cursor()
        sql = """CREATE TABLE empleados(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                dni INTEGER NOT NULL, cuil INTEGER NOT NULL, 
                nombres VARCHAR(30) NOT NULL, apellidos VARCHAR(30) NOT NULL,
                domicilio VARCHAR(30), f_nacimiento VARCHAR(10), f_alta VARCHAR(10),     
                obra VARCHAR(30), art VARCHAR(30), jornal FLOAT)"""
        cursor.execute(sql)
        self.conexion.commit()

    # ----- CONULTA A LA BASE DE DATOS -----
    def update_table(self, sql: str):
        self.sql = sql
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.sql)
        data_list = self.cursor.fetchall()
        return data_list

    # ----- MODIFICACION DE LA BASE DE DATOS -----
    def modify_table(self, sql: str, data: list):
        self.sql = sql
        self.data = data
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.sql, self.data)
        self.conexion.commit()
