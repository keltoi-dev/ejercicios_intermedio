import re
import sqlite3

# ##############################################
# MODELO
# ##############################################


# CONEXION CON LA BASE
class BaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("m2_u2_database.db")

    def hacer_tabla(self):
        self.cursor = self.conexion.cursor()
        sql = "CREATE TABLE compras(id integer PRIMARY KEY AUTOINCREMENT, \
        producto VARCHAR(20) NOT NULL, cantidad FLOAT, precio FLOAT)"
        self.cursor.execute(sql)
        self.conexion.commit()

    def consulta_base(self, sql, datos=""):
        self.sql = sql
        self.datos = datos
        self.cursor = self.conexion.cursor()
        if not datos:
            self.cursor.execute(self.sql)
        else:
            self.cursor.execute(self.sql, self.datos)
        self.la_lista = self.cursor.fetchall()
        return self.la_lista

    def guardar_base(self, sql, datos):
        self.sql = sql
        self.datos = datos
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.sql, self.datos)
        self.conexion.commit()


try:
    base = BaseDatos()
    base.hacer_tabla()
except:
    print("La base ya ha sido creada")


# ----- FUNCION DE ALTA -----
def alta(producto, cantidad, precio, tree):
    cadena = producto
    patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena
    if re.match(patron, cadena):
        datos = (producto, cantidad, precio)
        sql = "INSERT INTO compras(producto, cantidad, precio) VALUES (?, ?, ?)"
        base.guardar_base(sql, datos)

        total = calcular()
        print("Estoy en alta todo ok")
        actualizar_treeview(tree)
    else:
        print("error en campo producto")
    return total


# ----- FUNCION DE CONSULTA -----
def consultar(tree, a_val, b_val, c_val):
    item = tree.item(tree.selection())
    el_id = int(item["text"])
    datos = (el_id,)
    sql = "SELECT * FROM compras WHERE id = ?;"
    la_lista = base.consulta_base(sql, datos)
    a_val.set(la_lista[0][1])
    b_val.set(la_lista[0][2])
    c_val.set(la_lista[0][3])


# ----- FUNCION DE MODIFICACION -----
def modificar(tree, a_val, b_val, c_val):
    item = tree.item(tree.selection())
    el_id = int(item["text"])

    datos = (a_val, b_val, c_val, el_id)
    sql = "UPDATE compras SET producto = ?, cantidad = ?, precio = ? WHERE id = ?;"
    base.guardar_base(sql, datos)
    print("La seleccion fue modificada")
    total = calcular()
    actualizar_treeview(tree)
    return total


# ----- FUNCION DE BORRAR -----
def borrar(tree):
    valor = tree.selection()
    item = tree.item(valor)
    el_id = int(item["text"])
    datos = (el_id,)
    sql = "DELETE FROM compras WHERE id = ?;"
    base.guardar_base(sql, datos)

    total = calcular()
    print("La seleccion fue eliminada")
    tree.delete(valor)
    return total


# ----- FUNCION CALCULAR TOTAL -----
def calcular():
    total = 0
    sql = "SELECT * FROM compras ORDER BY id DESC;"
    la_lista = base.consulta_base(sql)
    for i in la_lista:
        total += i[2] * i[3]
    return total


# ----- FUNCION ACTUALIZAR TREE -----
def actualizar_treeview(mitreview):
    sql = "SELECT * FROM compras ORDER BY id DESC;"
    la_lista = base.consulta_base(sql)

    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    for fila in la_lista:
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))
