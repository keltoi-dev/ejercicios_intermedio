# Evaluación final
# Germán Fraga

from tkinter import Menu, Label, Button, Frame
from tkinter import StringVar, Entry
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkcalendar import DateEntry
import os
from modelo import create_record, close_app
from modelo import delete_record, modify_record
from modelo import search_record, update_treeview, consult_record
from modelo import conect_database, create_table


def base_window(window):
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

    Label(
        window, text="GESTION DE NOMINA DE EMPLEADOS", bg="#B9F582", font="Bold"
    ).grid(row=0, column=0, columnspan=2, sticky="w" + "e")

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
        row=0, column=0, sticky="w"
    )

    btn_alta = Button(
        frame_menu,
        text="ALTA",
        width=15,
        command=lambda: set_entry(
            create_record(create_list(), l_status, tree, var_filtro)
        ),
    )
    btn_alta.grid(row=1, column=0, padx=9, pady=8)
    btn_baja = Button(
        frame_menu,
        text="BAJA",
        width=15,
        command=lambda: set_entry(
            delete_record(create_list(), tree, l_status, var_filtro)
        ),
    )
    btn_baja.grid(row=2, column=0, padx=2, pady=9)
    btn_modificacion = Button(
        frame_menu,
        text="MODIFICACION",
        width=15,
        command=lambda: set_entry(
            modify_record(create_list(), tree, l_status, var_filtro)
        ),
    )
    btn_modificacion.grid(row=3, column=0, padx=2, pady=9)
    btn_consulta = Button(
        frame_menu,
        text="LIMPIAR",
        width=15,
        command=lambda: set_entry([["" for _ in range(11)] for _ in range(1)]),
    )
    btn_consulta.grid(row=4, column=0, padx=2, pady=9)
    btn_cerrar = Button(
        frame_menu, text="SALIR", width=15, command=lambda: close_app(window)
    )
    btn_cerrar.grid(row=5, column=0, padx=2, pady=8)

    # ----- FRAME DE DATOS -----
    frame_datos = Frame(window, padx=10, pady=10, bd=1, relief="solid")
    frame_datos.grid(row=1, column=1)

    Label(frame_datos, text="INFORMACION DEL EMPLEADO", font="Bold").grid(
        row=0, column=0, columnspan=6, pady=10, sticky="w"
    )

    Label(frame_datos, text="D.N.I.").grid(row=1, column=0, sticky="w")
    Label(frame_datos, text="C.U.I.L").grid(row=1, column=4, sticky="e")
    Label(frame_datos, text="NOMBRES").grid(row=2, column=0, sticky="w")
    Label(frame_datos, text="APELLIDOS").grid(row=3, column=0, sticky="w")
    Label(frame_datos, text="DOMICILIO").grid(row=4, column=0, sticky="w")
    Label(frame_datos, text="FECHA DE NAC.").grid(row=5, column=0, sticky="w")
    Label(frame_datos, text="FECHA DE ALTA").grid(row=5, column=4, sticky="e")
    Label(frame_datos, text="OBRA ASIGNADA").grid(row=6, column=0, sticky="w")
    Label(frame_datos, text="ART o SEGURO").grid(row=7, column=0, sticky="w")
    Label(frame_datos, text="JORNAL $").grid(row=8, column=0, sticky="w")
    Label(
        frame_datos,
        text="* En el campo DNI y CUIL solo ingrese números sin ',' o '-'.",
        fg="#ff1b1b",
    ).grid(row=9, column=1, columnspan=6, sticky="w")

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
        command=lambda: set_entry(search_record(var_dni.get(), l_status)),
    )
    btn_buscar.grid(row=1, column=2, sticky="w")

    # ----- FRAME PARA TREEVIEW -----
    frame_tree = Frame(window, padx=10, pady=10, bd=0, relief="solid")
    frame_tree.grid(row=2, column=0, columnspan=2)
    frame_tree.config(width=800, height=180)

    Label(frame_tree, text="FILTRAR POR OBRA").grid(row=0, column=0, sticky="e")

    e_filtro = Entry(frame_tree, textvariable=var_filtro, width=80)
    e_filtro.grid(row=0, column=1)

    btn_filtrar = Button(
        frame_tree,
        text="Filtrar",
        bg="#a1a1a1",
        command=lambda: update_treeview(
            tree, var_filtro, var_filtro.get().capitalize()
        ),
    )
    btn_filtrar.grid(row=0, column=2, sticky="w")

    tree = ttk.Treeview(frame_tree)
    tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
    tree.column("#0", width=35, minwidth=20, anchor="center")
    tree.column("col1", width=80, minwidth=50, anchor="center")
    tree.column("col2", width=200, minwidth=100)
    tree.column("col3", width=200, minwidth=100)
    tree.column("col4", width=180, minwidth=100)
    tree.column("col5", width=80, minwidth=60, anchor="e")
    tree.heading("#0", text="ID")
    tree.heading("col1", text="DNI")
    tree.heading("col2", text="NOMBRES")
    tree.heading("col3", text="APELLIDOS")
    tree.heading("col4", text="OBRA ASIGNADA")
    tree.heading("col5", text="JORNAL ($)")
    tree.grid(row=1, column=0, columnspan=3)
    tree.bind("<ButtonRelease-1>", lambda event: set_entry(consult_record(tree)))

    # ----- LABEL DE STATUS -----
    l_status = Label(window, text="Ok.", bg="#B9F582")
    l_status.grid(row=3, column=0, columnspan=2, sticky="w" + "e")

    try:
        conexion = conect_database()
        create_table(conexion, l_status)
        l_status.config(text="Se ha creado correctamente la base de datos.")
    except:
        l_status.config(
            text="La base de datos ya está creada. Se ha accedido correctamente."
        )

    update_treeview(tree, var_filtro)

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
