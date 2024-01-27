# Evaluación final
# Germán Fraga

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkcalendar import DateEntry
import sqlite3
import os
import re


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
def create_record(data: list):
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
                set_entry([["" for _ in range(11)] for _ in range(1)])
                l_status.config(
                    text="Los datos han sido guardados correctamente.",
                    background="#B9F582",
                )
                update_treeview(tree)
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


# ----- FUNCION DE BAJA DE REGISTRO -----
def delete_record(data: list, tree):
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
            update_treeview(tree)
            set_entry([["" for _ in range(11)] for _ in range(1)])
            l_status.config(
                text="Los datos han sido eliminados correctamente.",
                background="#B9F582",
            )
        else:
            l_status.config(
                text="Se ha cancelado la eliminación de los datos.",
                background="#B9F582",
            )


# ----- FUNCION DE MODIFICACION DE REGISTROS -----
def modify_record(data: list, tree):
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
            set_entry([["" for _ in range(11)] for _ in range(1)])
            l_status.config(
                text="Los datos han sido modificados correctamente.",
                background="#B9F582",
            )
            update_treeview(tree)
        else:
            l_status.config(
                text="Se ha cancelado la modificación de los datos.",
                background="#B9F582",
            )


# ***** FUNCIONES PARA CONSULTAS Y TREEVIEW *****
# ----- FUNCION DE CONSULTA DESDE TREEVIEW -----
def consult_record(event):
    item = tree.item(tree.selection())
    data = int(item["text"])
    sql = "SELECT * FROM empleados WHERE id = " + str(data)
    data_list = update_table(sql)
    set_entry(data_list)


# ----- FUNCION DE BUSQUEDA -----
def search_record(indice: str):
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
        set_entry(data_list)


# ----- FUNCION ACTUALIZAR TREEVIEW -----
def update_treeview(mitreview, parameter=None):
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
def close_app():
    option = askokcancel("Cerrar la aplicación", "¿Está seguro que quiere salir?")
    if option:
        window.destroy()


# ***** MANIPULACION DE DATOS *****
# ----- CREACION DE UNA LISTA PARA MOVIMIENTO DE LOS DATOS -----
def create_list():
    data_list = [
        var_dni.get(),
        var_cuil.get(),
        var_nombre.get(),
        var_apellido.get(),
        var_domicilio.get(),
        var_fnacimiento.get(),
        var_falta.get(),
        var_obra.get().capitalize(),
        var_art.get(),
        var_jornal.get(),
    ]
    return data_list


# ----- SETEO DE LOS ENTRY -----
def set_entry(data_list: list):
    var_dni.set(data_list[0][1])
    var_cuil.set(data_list[0][2])
    var_nombre.set(data_list[0][3])
    var_apellido.set(data_list[0][4])
    var_domicilio.set(data_list[0][5])
    var_fnacimiento.set(data_list[0][6])
    var_falta.set(data_list[0][7])
    var_obra.set(data_list[0][8])
    var_art.set(data_list[0][9])
    var_jornal.set(data_list[0][10])
    if not data_list[0][1]:
        l_status.config(text="Ok.", background="#B9F582")
        e_dni.config(state="normal")
        e_cuil.config(state="normal")
    else:
        l_status.config(
            text="Puede modificar o dar de baja al registro.", background="#B9F582"
        )
        e_dni.config(state="disabled")
        e_cuil.config(state="disabled")


# ----- DECLARACION DE TEXTO PARA VENTANA ACERCA DE ... -----
info = """
        Aplicación para el manejo de una base de datos con 
        altas, bajas, modificaciones y consultas (CRUD); 
        para una nómina de empleados con una gran variedad 
        de datos.
        
        AUTOR: Germán Fraga

        Entrega final - Diplomatura Python 3 - Nivel inicial
        26/12/2023
        """

# ***** VISTA Y CONTROL *****

window = Tk()
window.title("Evaluacion final - Python inicial")
# window.geometry("810x573")
window.resizable(False, False)
ruta = os.getcwd() + os.sep + "img" + os.sep
window.iconbitmap(ruta + "python.ico")

menubar = Menu(window, relief="solid")
menubar.add_cascade(
    label="Acerca de ...", command=lambda: showinfo("Acerca de ...", info)
)
window.config(menu=menubar)

Label(window, text="GESTION DE NOMINA DE EMPLEADOS", bg="#B9F582", font="Bold").grid(
    row=0, column=0, columnspan=2, sticky=W + E
)

# ----- DEFINICIONN DE VARIABLES -----
var_dni, var_cuil = StringVar(), StringVar()
var_nombre, var_apellido, var_domicilio = StringVar(), StringVar(), StringVar()
var_fnacimiento, var_falta = StringVar(), StringVar()
var_obra, var_art = StringVar(), StringVar()
var_jornal, var_filtro = StringVar(), StringVar()

# ----- FRAME DE MENU -----
frame_menu = Frame(window, bg="#a1a1a1", padx=10, pady=10, bd=1, relief="solid")
frame_menu.grid(row=1, column=0)

Label(frame_menu, text="MENU", bg="#a1a1a1", font="Bold").grid(
    row=0, column=0, sticky=W + E
)

btn_alta = Button(
    frame_menu, text="ALTA", width=15, command=lambda: create_record(create_list())
)
btn_alta.grid(row=1, column=0, padx=9, pady=8)
btn_baja = Button(
    frame_menu,
    text="BAJA",
    width=15,
    command=lambda: delete_record(create_list(), tree),
)
btn_baja.grid(row=2, column=0, padx=2, pady=9)
btn_modificacion = Button(
    frame_menu,
    text="MODIFICACION",
    width=15,
    command=lambda: modify_record(create_list(), tree),
)
btn_modificacion.grid(row=3, column=0, padx=2, pady=9)
btn_consulta = Button(
    frame_menu,
    text="LIMPIAR",
    width=15,
    command=lambda: set_entry([["" for _ in range(11)] for _ in range(1)]),
)
btn_consulta.grid(row=4, column=0, padx=2, pady=9)
btn_cerrar = Button(frame_menu, text="SALIR", width=15, command=lambda: close_app())
btn_cerrar.grid(row=5, column=0, padx=2, pady=8)

# ----- FRAME DE DATOS -----
frame_datos = Frame(window, padx=10, pady=10, bd=1, relief="solid")
frame_datos.grid(row=1, column=1)

Label(frame_datos, text="INFORMACION DEL EMPLEADO", font="Bold").grid(
    row=0, column=0, columnspan=6, pady=10, sticky=W + E
)

Label(frame_datos, text="D.N.I.").grid(row=1, column=0, sticky=W)
Label(frame_datos, text="C.U.I.L").grid(row=1, column=4, sticky=E)
Label(frame_datos, text="NOMBRES").grid(row=2, column=0, sticky=W)
Label(frame_datos, text="APELLIDOS").grid(row=3, column=0, sticky=W)
Label(frame_datos, text="DOMICILIO").grid(row=4, column=0, sticky=W)
Label(frame_datos, text="FECHA DE NAC.").grid(row=5, column=0, sticky=W)
Label(frame_datos, text="FECHA DE ALTA").grid(row=5, column=4, sticky=E)
Label(frame_datos, text="OBRA ASIGNADA").grid(row=6, column=0, sticky=W)
Label(frame_datos, text="ART o SEGURO").grid(row=7, column=0, sticky=W)
Label(frame_datos, text="JORNAL $").grid(row=8, column=0, sticky=W)
Label(
    frame_datos,
    text="* En el campo DNI y CUIL solo ingrese números sin ',' o '-'.",
    fg="#ff1b1b",
).grid(row=9, column=1, columnspan=6, sticky=W)

e_dni = Entry(frame_datos, textvariable=var_dni, width=15)
e_dni.grid(row=1, column=1)
e_cuil = Entry(frame_datos, textvariable=var_cuil, width=15)
e_cuil.grid(row=1, column=5)
e_nombre = Entry(frame_datos, textvariable=var_nombre, width=80)
e_nombre.grid(row=2, column=1, columnspan=5)
e_apellido = Entry(frame_datos, textvariable=var_apellido, width=80)
e_apellido.grid(row=3, column=1, columnspan=5)
e_direccion = Entry(frame_datos, textvariable=var_domicilio, width=80)
e_direccion.grid(row=4, column=1, columnspan=5)
e_fnacimiento = DateEntry(
    frame_datos,
    width=15,
    justify="center",
    date_pattern="dd-mm-yyyy",
    textvariable=var_fnacimiento,
    foreground="#000000",
)
e_fnacimiento.grid(row=5, column=1)
e_falta = DateEntry(
    frame_datos,
    width=15,
    justify="center",
    date_pattern="dd-mm-yyyy",
    textvariable=var_falta,
    foreground="#000000",
)
e_falta.grid(row=5, column=5)
e_obra = Entry(frame_datos, textvariable=var_obra, width=80)
e_obra.grid(row=6, column=1, columnspan=5)
e_art = Entry(frame_datos, textvariable=var_art, width=80)
e_art.grid(row=7, column=1, columnspan=5)
e_jornal = Entry(frame_datos, textvariable=var_jornal, width=15)
e_jornal.grid(row=8, column=1)

btn_buscar = Button(
    frame_datos,
    text="Buscar",
    width=6,
    bg="#a1a1a1",
    command=lambda: search_record(var_dni.get()),
)
btn_buscar.grid(row=1, column=2, sticky=W)

# ----- FRAME PARA TREEVIEW -----
frame_tree = Frame(window, padx=10, pady=10, bd=0, relief="solid")
frame_tree.grid(row=2, column=0, columnspan=2)
frame_tree.config(width=800, height=180)

Label(frame_tree, text="FILTRAR POR OBRA").grid(row=0, column=0, sticky=E)

e_filtro = Entry(frame_tree, textvariable=var_filtro, width=80)
e_filtro.grid(row=0, column=1)

btn_filtrar = Button(
    frame_tree,
    text="Filtrar",
    bg="#a1a1a1",
    command=lambda: update_treeview(tree, var_filtro.get().capitalize()),
)
btn_filtrar.grid(row=0, column=2, sticky=W)

tree = ttk.Treeview(frame_tree)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
tree.column("#0", width=35, minwidth=20, anchor="center")
tree.column("col1", width=80, minwidth=50, anchor="center")
tree.column("col2", width=200, minwidth=100)
tree.column("col3", width=200, minwidth=100)
tree.column("col4", width=180, minwidth=100)
tree.column("col5", width=80, minwidth=60, anchor=E)
tree.heading("#0", text="ID")
tree.heading("col1", text="DNI")
tree.heading("col2", text="NOMBRES")
tree.heading("col3", text="APELLIDOS")
tree.heading("col4", text="OBRA ASIGNADA")
tree.heading("col5", text="JORNAL ($)")
tree.grid(row=1, column=0, columnspan=3)
tree.bind("<ButtonRelease-1>", consult_record)

# ----- LABEL DE STATUS -----
l_status = Label(window, text="Ok.", bg="#B9F582")
l_status.grid(row=3, column=0, columnspan=2, sticky=W + E)

try:
    conexion = conect_database()
    create_table(conexion)
    l_status.config(text="Se ha creado correctamente la base de datos.")
except:
    l_status.config(
        text="La base de datos ya está creada. Se ha accedido correctamente."
    )

update_treeview(tree)

window.mainloop()
