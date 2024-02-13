import re
from base_datos import BaseDatos, DataBase
from auxiliares import AuxiliaresABM

# ##############################################
# MODELO
# ##############################################


class Abmc:
    def __init__(self, tree, nombre, tipo):
        self.tree = tree
        self.nombre = nombre
        self.tipo = tipo

        self.base = DataBase(self.nombre, self.tipo)
        self.db = BaseDatos()
        self.aux = AuxiliaresABM(tree, self.base)

        try:
            self.db.hacer_tabla()
            print(self.nombre, self.tipo)
        except:
            print("La base ya ha sido creada")

    # ----- FUNCION DE ALTA -----
    def alta(self, a_val, b_val, c_val):
        cadena = a_val
        patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena
        if re.match(patron, cadena):
            datos = (a_val, b_val, c_val)
            sql = "INSERT INTO compras(producto, cantidad, precio) VALUES (?, ?, ?)"
            self.db.guardar_base(sql, datos)

            print("Estoy en alta todo ok")
            self.aux.actualizar_treeview()

        else:
            print("error en campo producto")

        return self.aux.calcular()

    # ----- FUNCION DE CONSULTA -----
    def consultar(self, a_val, b_val, c_val):
        item = self.tree.item(self.tree.selection())
        el_id = int(item["text"])
        datos = (el_id,)
        sql = "SELECT * FROM compras WHERE id = ?;"
        la_lista = self.db.consulta_base(sql, datos)
        a_val.set(la_lista[0][1])
        b_val.set(la_lista[0][2])
        c_val.set(la_lista[0][3])

    # ----- FUNCION DE MODIFICACION -----
    def modificar(self, a_val, b_val, c_val):
        item = self.tree.item(self.tree.selection())
        el_id = int(item["text"])

        datos = (a_val, b_val, c_val, el_id)
        sql = "UPDATE compras SET producto = ?, cantidad = ?, precio = ? WHERE id = ?;"
        self.db.guardar_base(sql, datos)
        print("La seleccion fue modificada")
        total = self.aux.calcular()
        self.aux.actualizar_treeview()
        return total

    # ----- FUNCION DE BORRAR -----
    def borrar(self):
        valor = self.tree.selection()
        item = self.tree.item(valor)
        el_id = int(item["text"])
        datos = (el_id,)
        sql = "DELETE FROM compras WHERE id = ?;"
        self.db.guardar_base(sql, datos)

        total = self.aux.calcular()
        print("La seleccion fue eliminada")
        self.tree.delete(valor)
        return total
