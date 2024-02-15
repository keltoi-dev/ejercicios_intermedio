from tkinter import Label
from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import Entry
from tkinter import Button

from tkinter import ttk

from modelo import Abmc


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
        self.name_base = StringVar()
        self.type_base = StringVar()
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

        self.entrada4 = Entry(self.root, textvariable=self.name_base, width=w_ancho)
        self.entrada4.grid(row=1, column=3)

        self.entrada5 = ttk.Combobox(
            self.root,
            textvariable=self.type_base,
            width=17,
            state="readonly",
            values=["SQLite3", "MongoDB"],
        )
        self.entrada5.grid(row=2, column=3)

        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Producto")
        self.tree.heading("col2", text="cantidad")
        self.tree.heading("col3", text="precio")
        self.tree.grid(row=7, column=0, columnspan=4)

        self.wv = WidgetView(self.root)

        self.wv.boton_base("Comenzar", lambda: self.botones_habilitar(), 3, 3)

    def botones_habilitar(self):

        if self.name_base.get() and self.type_base.get():

            self.entrada1.config(state="normal")
            self.entrada2.config(state="normal")
            self.entrada3.config(state="normal")

            self.wv.boton_base(
                "Alta",
                lambda: self.t_val.set(
                    self.modelo.alta(
                        self.a_val.get(), self.b_val.get(), self.c_val.get()
                    )
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

            self.modelo = Abmc(
                self.tree, self.name_base.get(), self.type_base.get(), self.t_val
            )

            self.entrada4.config(state="disabled")
            self.entrada5.config(state="disabled")

        else:
            print("Debe completar el nombre de la base y el tipo")


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
