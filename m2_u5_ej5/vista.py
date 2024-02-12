from tkinter import Label
from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import Entry
from tkinter import Button

from tkinter import ttk

from auxiliares import AuxiliaresABM
from modelo import AlBaMo


# ##############################################
# VISTA
# ##############################################
class VentanaPrincipal:
    def __init__(self, root):
        self.root = root

    def ventana(self):
        self.root.title("Tarea con Base de Datos")

        titulo = Label(
            self.root,
            text="Ingrese sus datos",
            bg="DarkOrchid3",
            fg="thistle1",
            height=1,
            width=60,
        )
        titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e")

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val, self.c_val = StringVar(), DoubleVar(), DoubleVar()
        self.t_val = StringVar()
        name_base = StringVar
        type_base = StringVar
        w_ancho = 20

        producto = Label(self.root, text="Producto")
        producto.grid(row=1, column=0, sticky="w")
        cantidad = Label(self.root, text="Cantidad")
        cantidad.grid(row=2, column=0, sticky="w")
        precio = Label(self.root, text="Precio")
        precio.grid(row=3, column=0, sticky="w")
        l_total = Label(self.root, text="El total de la compra es:")
        l_total.grid(row=8, column=0, sticky="e", columnspan=3)

        n_base = Label(self.root, text="Nombre de la base")
        n_base.grid(row=1, column=2, sticky="e")
        t_base = Label(self.root, text="Tipo de base")
        t_base.grid(row=2, column=2, sticky="e")

        self.entrada1 = Entry(
            self.root, textvariable=self.a_val, width=w_ancho, state="disabled"
        )
        self.entrada1.grid(row=1, column=1)
        self.entrada2 = Entry(
            self.root, textvariable=self.b_val, width=w_ancho, state="disabled"
        )
        self.entrada2.grid(row=2, column=1)
        self.entrada3 = Entry(
            self.root, textvariable=self.c_val, width=w_ancho, state="disabled"
        )
        self.entrada3.grid(row=3, column=1)
        e_total = Entry(self.root, textvariable=self.t_val)
        e_total.grid(row=8, column=3)

        entrada4 = Entry(self.root, textvariable=name_base, width=w_ancho)
        entrada4.grid(row=1, column=3)

        entrada5 = Entry(self.root, textvariable=type_base, width=w_ancho)
        entrada5.grid(row=2, column=3)

        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------

        tree = ttk.Treeview(self.root)
        tree["columns"] = ("col1", "col2", "col3")
        tree.column("#0", width=90, minwidth=50, anchor="w")
        tree.column("col1", width=200, minwidth=80)
        tree.column("col2", width=200, minwidth=80)
        tree.column("col3", width=200, minwidth=80)
        tree.heading("#0", text="ID")
        tree.heading("col1", text="Producto")
        tree.heading("col2", text="cantidad")
        tree.heading("col3", text="precio")
        tree.grid(row=7, column=0, columnspan=4)

        self.modelo = AlBaMo(tree)
        aux = AuxiliaresABM(tree)
        self.wv = WidgetView(self.root)

        self.wv.boton_base("Comenzar", lambda: self.botones_habilitar(aux), 3, 3)

    def botones_habilitar(self, aux):
        self.aux = aux
        self.entrada1.config(state="normal")
        self.entrada2.config(state="normal")
        self.entrada3.config(state="normal")

        self.wv.boton_base(
            "Alta",
            lambda: self.t_val.set(
                self.modelo.alta(self.a_val.get(), self.b_val.get(), self.c_val.get())
            ),
            0,
        )

        self.wv.boton_base(
            "Consultar",
            lambda: self.modelo.consultar(self.a_val, self.b_val, self.c_val),
            1,
        )

        self.wv.boton_base(
            "Borrar",
            lambda: self.t_val.set(self.modelo.borrar()),
            2,
        )

        self.wv.boton_base(
            "Modificar",
            lambda: self.t_val.set(
                self.modelo.modificar(
                    self.a_val.get(), self.b_val.get(), self.c_val.get()
                )
            ),
            3,
        )

        self.t_val.set(self.aux.calcular())
        self.aux.actualizar_treeview()


class WidgetView(VentanaPrincipal):
    def __init__(self, root):
        super(WidgetView, self).__init__(root)

    def boton_base(self, texto, instruccion, x, y=6):
        self.texto = texto
        self.instruccion = instruccion
        self.x = x
        self.y = y

        self.btn_base = Button(self.root, text=self.texto, command=self.instruccion)
        self.btn_base.grid(row=self.y, column=self.x, sticky="w" + "e")
