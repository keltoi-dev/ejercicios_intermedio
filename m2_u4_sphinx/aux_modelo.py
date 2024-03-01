# Practicando POO
# Germán Fraga

from manejo_base import ManageBase
from verifica_campos import RegexCampos, RegexError


# ***** FUNCIONES PARA CONSULTAS Y TREEVIEW *****


class Auxiliares:
    def __init__(self) -> None:
        """
        Constructor de la clase para metodos auxiliares del modelo.
        Instancia el manejo de la base de datos.
        """
        self.base = ManageBase()

    # ----- FUNCION DE CONSULTA DESDE TREEVIEW -----
    def consult_record(self, tree: object) -> list:
        """ """
        self.tree = tree
        item = self.tree.item(self.tree.selection())
        data = item["values"][0]
        data_list = self.base.search_one(data)
        return data_list

    # ----- FUNCION DE BUSQUEDA -----
    def search_record(self, indice: str, l_status: object, aux_vista) -> tuple:
        self.indice = indice
        self.l_status = l_status
        self.aux_vista = aux_vista

        try:
            self.dni = RegexCampos("^\d{7,8}$", self.indice, "Busqueda de dni")
            self.dni.verificar()

            try:
                data_list = self.base.search_one(self.indice)
                self.l_status.config(
                    text="La búsqueda se concreto correctamente.", background="#B9F582"
                )
                self.aux_vista.set_entry(data_list)
                return None
            except:
                self.l_status.config(
                    text="No se encontró el DNI solicitado en la base de datos.",
                    background="#FF5656",
                )
                return "Este DNI no existe en la base de datos"

        except RegexError as log:
            log.guardar_error()
            self.l_status.config(
                text="Verifique los datos ingresados.", background="#FF5656"
            )
            return "La informacion cargada es incorrecta."

    # ----- FUNCION ACTUALIZAR TREEVIEW -----
    def update_treeview(self, mitreview: object, parameter: str = None) -> str:
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
