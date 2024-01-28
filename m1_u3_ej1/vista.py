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
        titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="WE")

        producto = Label(self.root, text="Producto")
        producto.grid(row=1, column=0, sticky="W")
        cantidad = Label(self.root, text="Cantidad")
        cantidad.grid(row=2, column=0, sticky="W")
        precio = Label(self.root, text="Precio")
        precio.grid(row=3, column=0, sticky="W")
        l_total = Label(self.root, text="El total de la compra es:")
        l_total.grid(row=12, column=0, sticky="E", columnspan=2)

        # Defino variables para tomar valores de campos de entrada
        a_val, b_val, c_val = StringVar(), DoubleVar(), DoubleVar()
        t_val = StringVar()
        w_ancho = 20

        entrada1 = Entry(self.root, textvariable=a_val, width=w_ancho)
        entrada1.grid(row=1, column=1)
        entrada2 = Entry(self.root, textvariable=b_val, width=w_ancho)
        entrada2.grid(row=2, column=1)
        entrada3 = Entry(self.root, textvariable=c_val, width=w_ancho)
        entrada3.grid(row=3, column=1)
        e_total = Entry(self.root, textvariable=t_val)
        e_total.grid(row=12, column=2)

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
        tree.grid(row=11, column=0, columnspan=3)

        modelo = AlBaMo(tree)
        aux = AuxiliaresABM(tree)

        boton_alta = Button(
            self.root,
            text="Alta",
            command=lambda: t_val.set(
                modelo.alta(a_val.get(), b_val.get(), c_val.get())
            ),
        )
        boton_alta.grid(row=6, column=1)

        boton_consulta = Button(
            self.root,
            text="Consultar",
            command=lambda: modelo.consultar(a_val, b_val, c_val),
        )
        boton_consulta.grid(row=7, column=1)

        boton_borrar = Button(
            self.root, text="Borrar", command=lambda: t_val.set(modelo.borrar())
        )
        boton_borrar.grid(row=8, column=1)

        boton_modificar = Button(
            self.root,
            text="Modifcar",
            command=lambda: t_val.set(
                modelo.modificar(a_val.get(), b_val.get(), c_val.get())
            ),
        )
        boton_modificar.grid(row=9, column=1)

        t_val.set(aux.calcular())
        aux.actualizar_treeview()
