"""
modelo.py:
    Modelo de la aplicacion - Altas, bajas y modificaciones
"""

from manejo_base import ManageBase
from aux_modelo import Auxiliares
from verifica_campos import RegexCampos, RegexError
from peewee import IntegrityError


# ***** FUNCIONES PARA ALTAS - BAJAS - MODIFICACIONES *****


class ManageData:
    def __init__(self, l_status: object, tree: object) -> None:
        self.l_status = l_status
        self.tree = tree
        self.aux = Auxiliares()
        self.base = ManageBase()

    # ----- FUNCION ALTA DE REGISTRO -----
    def create_record(self, data: list, aux_vista) -> tuple:
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
        self.data = data
        print(type(self.data[0]))
        self.base.delete_row(self.data[0])
        self.aux.update_treeview(self.tree)
        self.l_status.config(
            text="Los datos han sido eliminados correctamente.",
            background="#B9F582",
        )

        return [["" for _ in range(11)]]

    # ----- FUNCION DE MODIFICACION DE REGISTROS -----
    def modify_record(self, data: list) -> list:
        self.data = data
        self.base.modify_row(self.data)
        self.l_status.config(
            text="Los datos han sido modificados correctamente.",
            background="#B9F582",
        )
        self.aux.update_treeview(self.tree)

        return [["" for _ in range(11)]]
