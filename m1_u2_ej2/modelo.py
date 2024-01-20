import sqlite3
import os
import re
from tkinter.messagebox import showerror, askokcancel


# ***** FUNCIONES PARA MANEJO DE LA BASE DE DATOS *****
# ----- CONEXION CON LA BASE DE DATOS -----
def conect_database():
    ruta = os.getcwd() + os.sep + "src" + os.sep
    conexion = sqlite3.connect(ruta + "nomina_database.db")
    return conexion


# ----- CREACION DE LA TABLA DE LA BASE DE DATOS -----
def create_table(conexion):
    cursor = conexion.cursor()
    sql = """CREATE TABLE empleados(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            dni INTEGER NOT NULL, cuil INTEGER NOT NULL, 
            nombres VARCHAR(30) NOT NULL, apellidos VARCHAR(30) NOT NULL,
            domicilio VARCHAR(30), f_nacimiento VARCHAR(10), f_alta VARCHAR(10),     
            obra VARCHAR(30), art VARCHAR(30), jornal FLOAT)"""
    cursor.execute(sql)
    conexion.commit()


# ----- CONULTA A LA BASE DE DATOS -----
def update_table(sql: str):
    conexion = conect_database()
    cursor = conexion.cursor()
    cursor.execute(sql)
    data_list = cursor.fetchall()
    return data_list


# ----- MODIFICACION DE LA BASE DE DATOS -----
def modify_table(sql: str, data: list):
    conexion = conect_database()
    cursor = conexion.cursor()
    cursor.execute(sql, data)
    conexion.commit()


# ***** FUNCIONES PARA ALTAS - BAJAS - MODIFICACIONES *****
# ----- FUNCION ALTA DE REGISTRO -----
def create_record(data: list, l_status, tree, var_filtro):
    if not data[0] or not data[1] or not data[2] or not data[3]:
        l_status.config(text="Complete todos los campos.", background="#FF5656")
    else:
        cadena_dni, cadena_cuil = data[0], data[1]
        patron_dni, patron_cuil = "^\d{7,8}$", "^\d{11}$"
        if (re.match(patron_dni, cadena_dni)) and (re.match(patron_cuil, cadena_cuil)):
            sql = "SELECT * from empleados WHERE dni='" + data[0] + "';"
            data_list = update_table(sql)
            if not data_list:
                sql = """INSERT INTO empleados(dni, cuil, nombres, apellidos, 
                        domicilio, f_nacimiento, f_alta, obra, art, jornal) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                modify_table(sql, data)
                l_status.config(
                    text="Los datos han sido guardados correctamente.",
                    background="#B9F582",
                )
                update_treeview(tree, var_filtro)
            else:
                l_status.config(
                    text="El DNI ingresado ya está cargado en la base de datos.",
                    background="#FF5656",
                )
                showerror("ATENCIÓN!!", "El DNI ingresado ya fue cargado.")
        else:
            l_status.config(
                text="Verifique los datos ingresados.", background="#FF5656"
            )
            showerror("ATENCIÓN!!", "La informacion cargada es incorrecta.")
    return [["" for _ in range(11)] for _ in range(1)]


# ----- FUNCION DE BAJA DE REGISTRO -----
def delete_record(data: list, tree, l_status, var_filtro):
    if not data[0]:
        showerror("ATENCIÓN!!", "No se ha seleccionado ningún registro.")
        l_status.config(text="El campo DNI esta vacio.", background="#FF5656")
    else:
        sql = "DELETE FROM empleados WHERE dni = ?;"
        option = askokcancel(
            "Borra registro", "¿Está seguro que quiere eliminar ese registro?"
        )
        if option:
            modify_table(sql, (data[0],))
            update_treeview(tree, var_filtro)
            l_status.config(
                text="Los datos han sido eliminados correctamente.",
                background="#B9F582",
            )
        else:
            l_status.config(
                text="Se ha cancelado la eliminación de los datos.",
                background="#B9F582",
            )
    return [["" for _ in range(11)] for _ in range(1)]


# ----- FUNCION DE MODIFICACION DE REGISTROS -----
def modify_record(data: list, tree, l_status, var_filtro):
    if not data[0]:
        showerror("ATENCIÓN!!", "No se ha seleccionado ningún registro.")
        l_status.config(text="El campo DNI esta vacio.", background="#FF5656")
    else:
        sql = """UPDATE empleados SET nombres = ?, apellidos = ?, domicilio = ?, 
                f_nacimiento = ?, f_alta = ?, obra = ?, art = ?, 
                jornal = ? WHERE dni = ?;"""
        data.append(data[0])
        option = askokcancel(
            "Modifica registro", "¿Está seguro que quiere modificar ese registro?"
        )
        if option:
            for _ in range(2):
                data.pop(0)
            modify_table(sql, data)
            #            set_entry([["" for _ in range(11)] for _ in range(1)])
            l_status.config(
                text="Los datos han sido modificados correctamente.",
                background="#B9F582",
            )
            update_treeview(tree, var_filtro)
        else:
            l_status.config(
                text="Se ha cancelado la modificación de los datos.",
                background="#B9F582",
            )
    return [["" for _ in range(11)] for _ in range(1)]


# ***** FUNCIONES PARA CONSULTAS Y TREEVIEW *****
# ----- FUNCION DE CONSULTA DESDE TREEVIEW -----
def consult_record(tree):
    item = tree.item(tree.selection())
    data = int(item["text"])
    sql = "SELECT * FROM empleados WHERE id = " + str(data)
    data_list = update_table(sql)
    return data_list


# ----- FUNCION DE BUSQUEDA -----
def search_record(indice: str, l_status):
    sql = "SELECT * from empleados WHERE dni='" + indice + "';"
    data_list = update_table(sql)
    if not data_list:
        l_status.config(
            text="No se encontró el DNI solicitado en la base de datos.",
            background="#ff1b1b",
        )
        showerror("ATENCIÓN!!", "Este DNI no existe en la base de datos")
    else:
        l_status.config(
            text="La búsqueda se concreto correctamente.", background="#B9F582"
        )
    return data_list


# ----- FUNCION ACTUALIZAR TREEVIEW -----
def update_treeview(mitreview, var_filtro, parameter=None):
    if not parameter:
        sql = "SELECT id, dni, nombres, apellidos, obra, jornal FROM empleados ORDER BY id DESC;"
    else:
        sql = (
            "SELECT id, dni, nombres, apellidos, obra as 'Obra', jornal FROM empleados WHERE obra='"
            + parameter
            + "' ORDER BY id DESC;"
        )
    data_list = update_table(sql)

    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    for row in data_list:
        mitreview.insert(
            "", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5])
        )
    var_filtro.set("")


# ----- FUNCION DE CIERRE DE LA APLICACION -----
def close_app(window):
    option = askokcancel("Cerrar la aplicación", "¿Está seguro que quiere salir?")
    if option:
        window.destroy()
