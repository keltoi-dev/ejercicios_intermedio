# Evaluación final
# Germán Fraga

from tkinter import Menu, Label, Button, Frame
from tkinter import StringVar, Entry
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkcalendar import DateEntry
import os

from modelo import Auxiliares
from modelo import ManageData

aux = Auxiliares()


class MasterWindow:
    def __init__(self, window):
        self.window = window

    def base_window(self):
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
        self.window.title("Practicando POO - Python intermedio")
        # self.indow.geometry("810x573")
        self.window.resizable(False, False)
        ruta = os.getcwd() + os.sep + "img" + os.sep
        self.window.iconbitmap(ruta + "python.ico")

        menubar = Menu(self.window, relief="solid")
        menubar.add_cascade(
            label="Acerca de ...", command=lambda: showinfo("Acerca de ...", info)
        )
        self.window.config(menu=menubar)

        Label(
            self.window,
            text="GESTION DE NOMINA DE EMPLEADOS",
            bg="#B9F582",
            font="Bold",
        ).grid(row=0, column=0, columnspan=2, sticky="w" + "e")

        # ----- DEFINICIONN DE VARIABLES -----
        var_dni, var_cuil = StringVar(), StringVar()
        var_nombre, var_apellido, var_domicilio = StringVar(), StringVar(), StringVar()
        var_fnacimiento, var_falta = StringVar(), StringVar()
        var_obra, var_art = StringVar(), StringVar()
        var_jornal, var_filtro = StringVar(), StringVar()

        # ----- FRAME DE MENU -----
        frame_menu = Frame(
            self.window, bg="#a1a1a1", padx=10, pady=10, bd=1, relief="solid"
        )
        frame_menu.grid(row=1, column=0)

        Label(frame_menu, text="MENU", bg="#a1a1a1", font="Bold").grid(
            row=0, column=0, sticky="w"
        )

        btn_alta = Button(
            frame_menu,
            text="ALTA",
            width=15,
            command=lambda: vista.set_entry(modelo.create_record(vista.create_list())),
        )
        btn_alta.grid(row=1, column=0, padx=2, pady=9)
        btn_baja = Button(
            frame_menu,
            text="BAJA",
            width=15,
            command=lambda: vista.set_entry(modelo.delete_record(vista.create_list())),
        )
        btn_baja.grid(row=2, column=0, padx=2, pady=9)
        btn_modificacion = Button(
            frame_menu,
            text="MODIFICACION",
            width=15,
            command=lambda: vista.set_entry(modelo.modify_record(vista.create_list())),
        )
        btn_modificacion.grid(row=3, column=0, padx=2, pady=9)
        btn_consulta = Button(
            frame_menu,
            text="LIMPIAR",
            width=15,
            command=lambda: vista.set_entry(
                [["" for _ in range(11)] for _ in range(1)]
            ),
        )
        btn_consulta.grid(row=4, column=0, padx=2, pady=9)
        btn_cerrar = Button(
            frame_menu,
            text="SALIR",
            width=15,
            command=lambda: aux.close_app(self.window),
        )
        btn_cerrar.grid(row=5, column=0, padx=2, pady=8)

        # ----- FRAME DE DATOS -----
        frame_datos = Frame(self.window, padx=10, pady=10, bd=1, relief="solid")
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
            command=lambda: vista.set_entry(aux.search_record(var_dni.get(), l_status)),
        )
        btn_buscar.grid(row=1, column=2, sticky="w")

        # ----- FRAME PARA TREEVIEW -----
        frame_tree = Frame(self.window, padx=10, pady=10, bd=0, relief="solid")
        frame_tree.grid(row=2, column=0, columnspan=2)
        frame_tree.config(width=800, height=180)

        Label(frame_tree, text="FILTRAR POR OBRA").grid(row=0, column=0, sticky="e")

        e_filtro = Entry(frame_tree, textvariable=var_filtro, width=80)
        e_filtro.grid(row=0, column=1)

        btn_filtrar = Button(
            frame_tree,
            text="Filtrar",
            bg="#a1a1a1",
            command=lambda: aux.update_treeview(
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
        tree.bind(
            "<ButtonRelease-1>", lambda event: vista.set_entry(aux.consult_record(tree))
        )

        # ----- LABEL DE STATUS -----
        l_status = Label(self.window, text="Ok.", bg="#B9F582")
        l_status.grid(row=3, column=0, columnspan=2, sticky="w" + "e")

        l_status.config(text=aux.conect_database())

        # Instanciar objetos
        modelo = ManageData(l_status, tree, var_filtro)
        vista = AuxVista(
            var_dni,
            var_cuil,
            var_nombre,
            var_apellido,
            var_domicilio,
            var_fnacimiento,
            var_falta,
            var_art,
            var_obra,
            var_jornal,
            var_filtro,
            l_status,
            e_dni,
            e_cuil,
        )

        aux.update_treeview(tree, var_filtro)


class AuxVista(MasterWindow):
    def __init__(
        self,
        var_dni,
        var_cuil,
        var_nombre,
        var_apellido,
        var_domicilio,
        var_fnacimiento,
        var_falta,
        var_art,
        var_obra,
        var_jornal,
        var_filtro,
        l_status,
        e_dni,
        e_cuil,
    ):
        self.var_dni = var_dni
        self.var_cuil = var_cuil
        self.var_nombre = var_nombre
        self.var_apellido = var_apellido
        self.var_domicilio = var_domicilio
        self.var_fnacimiento = var_fnacimiento
        self.var_falta = var_falta
        self.var_art = var_art
        self.var_obra = var_obra
        self.var_jornal = var_jornal
        self.var_filtro = var_filtro
        self.l_status = l_status
        self.e_dni = e_dni
        self.e_cuil = e_cuil

    # ***** MANIPULACION DE DATOS *****
    # ----- CREACION DE UNA LISTA PARA MOVIMIENTO DE LOS DATOS -----
    def create_list(self):
        data_list = [
            self.var_dni.get(),
            self.var_cuil.get(),
            self.var_nombre.get(),
            self.var_apellido.get(),
            self.var_domicilio.get(),
            self.var_fnacimiento.get(),
            self.var_falta.get(),
            self.var_obra.get().capitalize(),
            self.var_art.get(),
            self.var_jornal.get(),
        ]
        return data_list

    # ----- SETEO DE LOS ENTRY -----
    def set_entry(self, data_list: list):
        if data_list[0][1] != "a":
            self.var_dni.set(data_list[0][1])
            self.var_cuil.set(data_list[0][2])
            self.var_nombre.set(data_list[0][3])
            self.var_apellido.set(data_list[0][4])
            self.var_domicilio.set(data_list[0][5])
            self.var_fnacimiento.set(data_list[0][6])
            self.var_falta.set(data_list[0][7])
            self.var_obra.set(data_list[0][8])
            self.var_art.set(data_list[0][9])
            self.var_jornal.set(data_list[0][10])
            if not data_list[0][1]:
                self.l_status.config(text="Ok.", background="#B9F582")
                self.e_dni.config(state="normal")
                self.e_cuil.config(state="normal")
            else:
                self.l_status.config(
                    text="Puede modificar o dar de baja al registro.",
                    background="#B9F582",
                )
                self.e_dni.config(state="disabled")
                self.e_cuil.config(state="disabled")
