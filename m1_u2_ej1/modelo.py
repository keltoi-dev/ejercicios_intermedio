import re
import sqlite3

# ##############################################
# MODELO
# ##############################################


# CONEXION CON LA BASE
def conectar_base():
    conexion = sqlite3.connect("m2_u2_database.db")
    return conexion


def hacer_tabla(conexion):
    cursor = conexion.cursor()
    sql = "CREATE TABLE compras(id integer PRIMARY KEY AUTOINCREMENT, \
    producto VARCHAR(20) NOT NULL, cantidad FLOAT, precio FLOAT)"
    cursor.execute(sql)
    conexion.commit()


def consulta_base():
    conexion = conectar_base()
    cursor = conexion.cursor()
    sql = "SELECT * FROM compras ORDER BY id DESC;"
    cursor.execute(sql)
    la_lista = cursor.fetchall()
    return la_lista


# ----- FUNCION DE ALTA -----
def alta(producto, cantidad, precio, tree):
    cadena = producto
    patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena
    if re.match(patron, cadena):
        conexion = conectar_base()
        cursor = conexion.cursor()
        datos = (producto, cantidad, precio)
        sql = "INSERT INTO compras(producto, cantidad, precio) VALUES (?, ?, ?)"
        cursor.execute(sql, datos)
        conexion.commit()

        total = calcular()
        print("Estoy en alta todo ok")
        actualizar_treeview(tree)
    else:
        print("error en campo producto")
    return total


# ----- FUNCION CALCULAR TOTAL -----
def calcular():
    total = 0
    la_lista = consulta_base()
    for i in la_lista:
        total += i[2] * i[3]
    return total


# ----- FUNCION DE CONSULTA -----
def consultar(tree, a_val, b_val, c_val):
    item = tree.item(tree.selection())
    conexion = conectar_base()
    cursor = conexion.cursor()
    el_id = int(item["text"])
    datos = (el_id,)
    sql = "SELECT * FROM compras WHERE id = ?;"
    cursor.execute(sql, datos)
    la_lista = cursor.fetchall()
    a_val.set(la_lista[0][1])
    b_val.set(la_lista[0][2])
    c_val.set(la_lista[0][3])


# ----- FUNCION DE MODIFICACION -----
def modificar(tree, producto, cantidad, precio):
    item = tree.item(tree.selection())
    el_id = int(item["text"])

    conexion = conectar_base()
    cursor = conexion.cursor()

    datos = (producto, cantidad, precio, el_id)
    sql = "UPDATE compras SET producto = ?, cantidad = ?, precio = ? WHERE id = ?;"
    cursor.execute(sql, datos)
    conexion.commit()
    print("La seleccion fue modificada")
    total = calcular()
    actualizar_treeview(tree)
    return total


# ----- FUNCION DE BORRAR -----
def borrar(tree):
    valor = tree.selection()
    item = tree.item(valor)
    conexion = conectar_base()
    cursor = conexion.cursor()
    el_id = int(item["text"])
    datos = (el_id,)
    sql = "DELETE FROM compras WHERE id = ?;"
    cursor.execute(sql, datos)
    conexion.commit()

    total = calcular()
    print("La seleccion fue eliminada")
    tree.delete(valor)
    return total


# ----- FUNCION ACTUALIZAR TREE -----
def actualizar_treeview(mitreview):
    la_lista = consulta_base()

    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    for fila in la_lista:
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))
