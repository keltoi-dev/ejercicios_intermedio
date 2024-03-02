"""
aux_modelo.py:
    Contiene funciones auxiliares al modelo, como la actulalización del treeview, consulta de
    un registro desde el treeview y consulta desde el campo de dni.
"""

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
        """
        Hace una busqueda de un registro desde la selección en el treeview.
        Consulta la base de datos a través del método del ORM filtando por el id.

        :param tree: Objeto de la vista que contiene la información de la base de datos
        :returns: Una lista con toda la información del registro
        :rtype: list[str, int]
        """
        self.tree = tree
        item = self.tree.item(self.tree.selection())
        data = item["values"][0]
        data_list = self.base.search_one(data)
        return data_list

    # ----- FUNCION DE BUSQUEDA -----
    def search_record(self, indice: str, l_status: object, aux_vista: object) -> str:
        """
        Hace una búsqueda de un número de dni desde el entry de este dato.
        Verifica que el dato ingresado cumpla con los requisitos del regex indicado en la instancia.
        Se utilizan excepciones que retornan la información sobre el error.

        :param indice: Es el dato del número de DNI
        :param l_status: Objeto de tkinter, etiqueta para la información en la barra de status
        :param aux_vista: Objeto instanciado auxiliar de la vista
        :returns: Un texto con la información sobre el posible error
        :rtype: str
        """
        self.indice = indice
        self.l_status = l_status
        self.aux_vista = aux_vista

        try:
            self.dni = RegexCampos("^\d{7,8}$", self.indice, "Búsqueda de dni")
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
            return "La información cargada es incorrecta."

    # ----- FUNCION ACTUALIZAR TREEVIEW -----
    def update_treeview(self, mitreview: object, parameter: str = None) -> str:
        """
        Función para actualizar la información contenida en el treeview luego de cualquier cambio en
        la base de datos. Ya sea con toda la información o aplicando un filtro de busqueda por obra.

        :param mitreeview: Objeto de la vista que contiene la información de la base de datos
        :param parameter: String con el dato del entry filtro para seleccionar los registros
        :returns: Texto vacio para la limpieza del campo de búsqueda
        :rtype: str
        """
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
