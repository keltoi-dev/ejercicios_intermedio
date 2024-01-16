from tkinter import Label
from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import Entry
from tkinter import Button

from tkinter import ttk

from modelo import (
    conectar_base,
    hacer_tabla,
    alta,
    calcular,
    consultar,
    modificar,
    borrar,
    actualizar_treeview,
)


try:
    conexion = conectar_base()
    hacer_tabla(conexion)
except:
    print("La base ya ha sido creada")


# ##############################################
# VISTA
# ##############################################
def ventana(root):
    root.title("Tarea con Base de Datos")

    titulo = Label(
        root,
        text="Ingrese sus datos",
        bg="DarkOrchid3",
        fg="thistle1",
        height=1,
        width=60,
    )
    titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="WE")

    producto = Label(root, text="Producto")
    producto.grid(row=1, column=0, sticky="W")
    cantidad = Label(root, text="Cantidad")
    cantidad.grid(row=2, column=0, sticky="W")
    precio = Label(root, text="Precio")
    precio.grid(row=3, column=0, sticky="W")
    l_total = Label(root, text="El total de la compra es:")
    l_total.grid(row=12, column=0, sticky="E", columnspan=2)

    # Defino variables para tomar valores de campos de entrada
    a_val, b_val, c_val = StringVar(), DoubleVar(), DoubleVar()
    t_val = StringVar()
    w_ancho = 20

    entrada1 = Entry(root, textvariable=a_val, width=w_ancho)
    entrada1.grid(row=1, column=1)
    entrada2 = Entry(root, textvariable=b_val, width=w_ancho)
    entrada2.grid(row=2, column=1)
    entrada3 = Entry(root, textvariable=c_val, width=w_ancho)
    entrada3.grid(row=3, column=1)
    e_total = Entry(root, textvariable=t_val)
    e_total.grid(row=12, column=2)

    # --------------------------------------------------
    # TREEVIEW
    # --------------------------------------------------

    tree = ttk.Treeview(root)
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

    boton_alta = Button(
        root,
        text="Alta",
        command=lambda: t_val.set(alta(a_val.get(), b_val.get(), c_val.get(), tree)),
    )
    boton_alta.grid(row=6, column=1)

    boton_consulta = Button(
        root, text="Consultar", command=lambda: consultar(tree, a_val, b_val, c_val)
    )
    boton_consulta.grid(row=7, column=1)

    boton_borrar = Button(root, text="Borrar", command=lambda: t_val.set(borrar(tree)))
    boton_borrar.grid(row=8, column=1)

    boton_modificar = Button(
        root,
        text="Modifcar",
        command=lambda: t_val.set(
            modificar(tree, a_val.get(), b_val.get(), c_val.get())
        ),
    )
    boton_modificar.grid(row=9, column=1)

    t_val.set(calcular())
    actualizar_treeview(tree)
