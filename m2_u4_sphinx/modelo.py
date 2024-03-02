"""
modelo.py:
    Modelo de la aplicación - Altas, bajas y modificaciones
"""

from manejo_base import ManageBase, BaseError
from aux_modelo import Auxiliares
from verifica_campos import RegexCampos, RegexError
from peewee import IntegrityError


# ***** FUNCIONES PARA ALTAS - BAJAS - MODIFICACIONES *****


class ManageData:
    def __init__(self, l_status: object, tree: object) -> None:
        """
        Constructor de la clase de manejo de datos CRUD

        :param l_status: Objeto de tkinter, label para información
        :param tree: Objeto de tkinter treeview, tabla que muestra el contenido de la base de datos
        """
        self.l_status = l_status
        self.tree = tree
        self.aux = Auxiliares()
        self.base = ManageBase()

    # ----- FUNCION ALTA DE REGISTRO -----
    def create_record(self, data: list, aux_vista) -> str:
        """
        Función de alta de los datos capturados en una lista de los campos entry de la vista.
        Verifica que los campos dni, cuil, nombre y apellido no esten vacios.
        Instancia RegexCampos en la variable dni y cuil para control de estos campos.
        Accede al método del ORM para grabar los datos en la tabla de la base sqlite3.
        Actualiza el treeview y vacia los campos entry de la vista.
        En caso de error retorna textos con el detalle del error, de acuerdo al manejo de las excepciones.

        :param data: Lista con la información de los campos
        :param aux_vista: Objeto que llega desde el módulo vista
        :returns: un texto para la información de los message error
        :rtype: str
        """
        self.data = data
        self.aux_vista = aux_vista
        if not self.data[0] or not self.data[1] or not self.data[2] or not self.data[3]:
            self.l_status.config(
                text="Complete todos los campos.", background="#FF5656"
            )

        else:
            try:
                self.dni = RegexCampos("^\d{7,8}$", self.data[0], "Dni en alta")
                self.cuil = RegexCampos("^\d{11}$", self.data[1], "CUIL en alta")
                self.dni.verificar()
                self.cuil.verificar()

                try:
                    self.base.save_row(data)
                    self.l_status.config(
                        text="Los datos han sido guardados correctamente.",
                        background="#B9F582",
                    )
                    self.aux.update_treeview(self.tree)
                    self.aux_vista.set_entry([["" for _ in range(11)]])
                    return None
                except IntegrityError:
                    BaseError().guardar_error()
                    self.l_status.config(
                        text="El DNI ingresado ya está cargado en la base de datos.",
                        background="#FF5656",
                    )
                    return "El DNI ingresado ya fue cargado."

            except RegexError as log:
                log.guardar_error()
                self.l_status.config(
                    text="Verifique los datos ingresados.", background="#FF5656"
                )
                return "La informacion cargada es incorrecta."

    # ----- FUNCION DE BAJA DE REGISTRO -----
    def delete_record(self, data: list) -> list:
        """
        Funcion de baja de registro seleccionado de la base de datos.
        Recibe la informacion del metodo auxiliar de la vista.
        Llama al metodo del ORM para eliminar la fila de la base de datos.
        Actualiza el treeview e informa en la barra de status la accion.

        :param data: Lista con la informacion de los campos
        :returns: Una lista vacia para limpieza de los campos
        """
        self.data = data
        self.base.delete_row(self.data[0])
        self.aux.update_treeview(self.tree)
        self.l_status.config(
            text="Los datos han sido eliminados correctamente.",
            background="#B9F582",
        )

        return [["" for _ in range(11)]]

    # ----- FUNCION DE MODIFICACION DE REGISTROS -----
    def modify_record(self, data: list) -> list:
        """
        Funcion para la modificacion del registro seleccionado de la base de datos.
        Los datos los recibe del metodo auxiliar de la vista.
        Llama al metodo del ORM para el update de la fila en la base de datos.

        :param data: Lista con la informacion de los campos
        :returns: Una lista vacia para limpieza de los campos
        """
        self.data = data
        self.base.modify_row(self.data)
        self.l_status.config(
            text="Los datos han sido modificados correctamente.",
            background="#B9F582",
        )
        self.aux.update_treeview(self.tree)

        return [["" for _ in range(11)]]
