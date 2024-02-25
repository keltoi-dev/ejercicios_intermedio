"""
vista.py:
    Costructor de la interfaz con el usuario
"""

from tkinter import Menu, Label, Button, Frame
from tkinter import StringVar, Entry
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkcalendar import DateEntry
from tkinter.messagebox import showerror, askokcancel
import os

from aux_modelo import Auxiliares
from modelo import ManageData
from aux_vista import AuxVista

# Instancia del modulo auxiliar del modelo
aux = Auxiliares()


class MasterWindow:
    def __init__(self, window: object) -> None:
        """
        Armado de la ventana de tkinter
        :param window: objeto de Tk
        """
        self.window = window

    def base_window(self) -> None:

        # ----- DECLARACION DE TEXTO PARA VENTANA ACERCA DE ... -----
        info = """
                Aplicación para el manejo de una base de datos con 
                altas, bajas, modificaciones y consultas (CRUD); 
                para una nómina de empleados con una gran 
                variedad de datos.
                
                AUTOR: Germán Fraga

                Practicando POO
                Diplomatura Python 3 - Nivel intermedio
                23/2/2024
                """

        # Construccion de la ventana principal
        self.window.title("Practicando POO - Python intermedio")
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
        widget_1 = WidgetsWindows(frame_menu)
        widget_1.boton_1(
            "ALTA",
            lambda: self.create_record_view(),
            1,
        )
        widget_1.boton_1(
            "BAJA",
            lambda: self.delete_record_view(),
            2,
        )
        widget_1.boton_1(
            "MODIFICACION",
            lambda: self.modify_record_view(),
            3,
        )
        widget_1.boton_1(
            "LIMPIAR",
            lambda: self.vista.set_entry([["" for _ in range(11)]]),
            4,
        )
        widget_1.boton_1(
            "SALIR",
            lambda: self.vista.close_app(self.window),
            5,
        )

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
        widget_2 = WidgetsWindows(frame_datos)

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

        widget_2.date_in(var_fnacimiento, 1)
        widget_2.date_in(var_falta, 5)

        e_obra = Entry(frame_datos, textvariable=var_obra, width=80)
        e_obra.grid(row=6, column=1, columnspan=5)
        e_art = Entry(frame_datos, textvariable=var_art, width=80)
        e_art.grid(row=7, column=1, columnspan=5)
        e_jornal = Entry(frame_datos, textvariable=var_jornal, width=15)
        e_jornal.grid(row=8, column=1)

        widget_2.boton_2(
            "Buscar",
            lambda: self.search_record_view(var_dni),
            1,
        )

        # ----- FRAME PARA TREEVIEW -----
        frame_tree = Frame(self.window, padx=10, pady=10, bd=0, relief="solid")
        frame_tree.grid(row=2, column=0, columnspan=2)
        frame_tree.config(width=800, height=180)

        Label(frame_tree, text="FILTRAR POR OBRA").grid(row=0, column=0, sticky="e")

        e_filtro = Entry(frame_tree, textvariable=var_filtro, width=80)
        e_filtro.grid(row=0, column=1)

        wid_btn2 = WidgetsWindows(frame_tree)
        wid_btn2.boton_2(
            "Filtrar",
            lambda: self.vista.var_filtro.set(
                aux.update_treeview(tree, var_filtro.get().capitalize())
            ),
            0,
        )

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
            "<ButtonRelease-1>",
            lambda event: self.vista.set_entry(aux.consult_record(tree)),
        )

        # ----- LABEL DE STATUS -----
        self.l_status = Label(self.window, text="Ok.", bg="#B9F582")
        self.l_status.grid(row=3, column=0, columnspan=2, sticky="w" + "e")

        # Instanciar objetos - Modulo del modelo y auxiliar de la vista
        self.modelo = ManageData(self.l_status, tree)
        self.vista = AuxVista(
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
            self.l_status,
            e_dni,
            e_cuil,
        )

        aux.update_treeview(tree, var_filtro.get())

    # Funciones auxiliares para llamada a modelo y retorno de errores
    def create_record_view(self) -> None:
        """
        Control de la informacion para el alta llamando al modulo modelo - create_record
        Advertencia de errores con ventanas emergentes showeror
        :param: None
        """
        data, info = self.modelo.create_record(self.vista.create_list())

        if info:
            showerror("ATENCIÓN!!", info)
        else:
            self.vista.set_entry(data)

    def delete_record_view(self) -> None:
        """
        Control de la informacion para la baja llamando al modulo modelo - delete_record
        Advertencia de errores con ventanas emergentes showeror y confirmacion con askokcancel
        :param: None
        """
        data_list = self.vista.create_list()
        if not data_list[0]:
            showerror("ATENCIÓN!!", "No se ha seleccionado ningún registro.")
            self.l_status.config(text="El campo DNI esta vacio.", background="#FF5656")
        else:
            option = askokcancel(
                "Borra registro", "¿Está seguro que quiere eliminar ese registro?"
            )
            if option:
                self.vista.set_entry(self.modelo.delete_record(data_list))
            else:
                self.l_status.config(
                    text="Se ha cancelado la eliminación de los datos.",
                    background="#B9F582",
                )

    def modify_record_view(self) -> None:
        """
        Control de la informacion para modificaciones llamando al modulo modelo - modify_record
        Advertencia de errores con ventanas emergentes showeror y confirmacion con askokcancel
        :param: None
        """
        data_list = self.vista.create_list()
        if not data_list[0]:
            showerror("ATENCIÓN!!", "No se ha seleccionado ningún registro.")
            self.l_status.config(text="El campo DNI esta vacio.", background="#FF5656")
        else:
            option = askokcancel(
                "Modifica registro", "¿Está seguro que quiere modificar ese registro?"
            )
            if option:
                self.vista.set_entry(self.modelo.modify_record(data_list))
            else:
                self.l_status.config(
                    text="Se ha cancelado la modificación de los datos.",
                    background="#B9F582",
                )

    def search_record_view(self, var_dni: object) -> None:
        """
        Control de la informacion para busqueda llamando al modulo auxiliar de modelo - search_record
        Advertencia de errores con ventanas emergentes showeror y confirmacion con askokcancel
        :param var_dni: Objeto entry del frame datos
        """
        data, info = aux.search_record(var_dni.get(), self.l_status)
        if info:
            showerror("ATENCIÓN!!", info)
        else:
            self.vista.set_entry(data)


class WidgetsWindows(MasterWindow):
    def __init__(self, frame: object) -> None:
        """
        Creacion de los objetos para los widgets de la vista
        :param frame: Objeto contenedor de tkinter
        """
        self.frame = frame

    def boton_1(self, text_btn: str, instruction: str, position: int) -> None:
        """
        Objeto para generar botones de tkinter
        :param text_btn: Texto del boton
        :param instruction: Funcion lambda para ejecutar desde el boton
        :param position: Valor de la fila del boton
        """
        self.text_btn = text_btn
        self.instruction = instruction
        self.position = position
        self.btn = Button(
            self.frame,
            text=self.text_btn,
            width=15,
            command=self.instruction,
        )
        self.btn.grid(row=self.position, column=0, padx=2, pady=9)

    def boton_2(self, text_btn: str, instruction: str, position: int) -> None:
        """
        Objeto para generar botones grises de tkinter
        :param text_btn: Texto del boton
        :param instruction: Funcion lambda para ejecutar desde el boton
        :param position: Valor de la fila del boton
        """
        self.text_btn = text_btn
        self.instruction = instruction
        self.position = position
        btn_buscar = Button(
            self.frame,
            text=self.text_btn,
            width=6,
            bg="#a1a1a1",
            command=self.instruction,
        )
        btn_buscar.grid(row=self.position, column=2, sticky="w")

    def date_in(self, data_var: object, position: int) -> None:
        """
        Objeto para almanaque para carga de fechas de tkcalendar
        :param data_var: Variable para tomar la fecha
        :param position: Valor de la fila del boton
        """
        self.data_var = data_var
        self.position = position
        e_fecha = DateEntry(
            self.frame,
            width=15,
            justify="center",
            date_pattern="dd-mm-yyyy",
            textvariable=self.data_var,
            foreground="#000000",
        )
        e_fecha.grid(row=5, column=self.position)
