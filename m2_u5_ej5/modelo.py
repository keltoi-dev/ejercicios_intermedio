import re
from base_datos import BaseDatos, DataBase, Mongo
from auxiliares import AuxiliaresABM

# ##############################################
# MODELO
# ##############################################


class Abmc:
    def __init__(self, tree, nombre, tipo, t_val):
        self.tree = tree
        self.nombre = nombre
        self.tipo = tipo
        self.t_val = t_val

        self.database = DataBase(self.nombre)
        if self.tipo == "SQLite3":
            self.db = BaseDatos(self.nombre)
            try:
                self.db.hacer_tabla()
            except:
                print("La base ya ha sido creada")
        else:
            self.db = Mongo(self.nombre)
            self.db.hacer_tabla()

        self.aux = AuxiliaresABM(self.tree, self.db)

        self.aux.actualizar_treeview()
        self.t_val.set(self.aux.calcular())

    # ----- FUNCION DE ALTA -----
    def alta(self, a_val, b_val, c_val):
        cadena = a_val
        patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena
        if re.match(patron, cadena):
            datos = (a_val, b_val, c_val)

            self.db.incorporar_base(datos)

            print("Estoy en alta todo ok")
            self.aux.actualizar_treeview()

        else:
            print("error en campo producto")

        return self.aux.calcular()

    # ----- FUNCION DE CONSULTA -----
    def consultar(self, a_val, b_val, c_val):
        item = self.tree.item(self.tree.selection())
        if self.tipo == "SQLite3":
            el_id = int(item["text"])
            datos = (el_id,)
        else:
            datos = item["values"][0]
        la_lista = self.db.consulta_uno(datos)
        a_val.set(la_lista[0][1])
        b_val.set(la_lista[0][2])
        c_val.set(la_lista[0][3])

    # ----- FUNCION DE MODIFICACION -----
    def modificar(self, a_val, b_val, c_val):
        item = self.tree.item(self.tree.selection())
        if self.tipo == "SQLite3":
            el_id = int(item["text"])
        else:
            el_id = item["values"][0]

        datos = (a_val, b_val, c_val, el_id)
        self.db.modificar_base(datos)
        print("La seleccion fue modificada")
        total = self.aux.calcular()
        self.aux.actualizar_treeview()
        return total

    # ----- FUNCION DE BORRAR -----
    def borrar(self):
        valor = self.tree.selection()
        item = self.tree.item(valor)
        if self.tipo == "SQLite3":
            el_id = int(item["text"])
            datos = (el_id,)
        else:
            datos = item["values"][0]

        self.db.borrar_base(datos)

        total = self.aux.calcular()
        print("La seleccion fue eliminada")
        self.tree.delete(valor)
        return total
