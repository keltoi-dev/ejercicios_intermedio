from base_datos import BaseDatos


class AuxiliaresABM:
    def __init__(self, tree, db):
        self.tree = tree
        self.base = db

    # ----- FUNCION CALCULAR TOTAL -----
    def calcular(self):
        total = 0
        la_lista = self.base.consulta_todo()
        for i in la_lista:
            total += i[2] * i[3]
        return total

    # ----- FUNCION ACTUALIZAR TREE -----
    def actualizar_treeview(self):
        la_lista = self.base.consulta_todo()

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        for fila in la_lista:
            self.tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))
