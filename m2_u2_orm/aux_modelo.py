# Practicando POO
# Germán Fraga

from manejo_base import ManageBase
from tkinter.messagebox import showerror, askokcancel
from verifica_campos import RegexCampos


# ***** FUNCIONES PARA CONSULTAS Y TREEVIEW *****


class Auxiliares:
    def __init__(self):
        self.base = ManageBase()
        self.control = RegexCampos()

    # ----- FUNCION DE CONSULTA DESDE TREEVIEW -----
    def consult_record(self, tree) -> list:
        self.tree = tree
        item = self.tree.item(self.tree.selection())
        data = item["values"][0]
        data_list = self.base.search_one(data)
        return data_list

    # ----- FUNCION DE BUSQUEDA -----
    def search_record(self, indice: str, l_status) -> list:
        self.indice = indice
        self.l_status = l_status
        if self.control.verificar("^\d{7,8}$", self.indice):
            try:
                data_list = self.base.search_one(self.indice)
                self.l_status.config(
                    text="La búsqueda se concreto correctamente.", background="#B9F582"
                )
                return data_list
            except:
                self.l_status.config(
                    text="No se encontró el DNI solicitado en la base de datos.",
                    background="#FF5656",
                )
                showerror("ATENCIÓN!!", "Este DNI no existe en la base de datos")
                return [["-" for _ in range(11)]]
        else:
            self.l_status.config(
                text="Verifique los datos ingresados.", background="#FF5656"
            )
            showerror("ATENCIÓN!!", "La informacion cargada es incorrecta.")
            return [["-" for _ in range(11)]]

    # ----- FUNCION ACTUALIZAR TREEVIEW -----
    def update_treeview(self, mitreview, parameter: str = None) -> str:
        self.mitreview = mitreview
        self.parameter = parameter
        if not parameter:
            data_list = self.base.update_table()
        else:
            data_list = self.base.filter_table(self.parameter)

        records = self.mitreview.get_children()
        for element in records:
            self.mitreview.delete(element)

        for row in data_list:
            self.mitreview.insert(
                "",
                0,
                text=row.id,
                values=(row.dni, row.nombres, row.apellidos, row.obra, row.jornal),
            )
        return ""

    # ----- FUNCION DE CIERRE DE LA APLICACION -----
    def close_app(self, window):
        option = askokcancel("Cerrar la aplicación", "¿Está seguro que quiere salir?")
        if option:
            window.destroy()
