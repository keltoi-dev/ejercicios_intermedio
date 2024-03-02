"""
aux_vista.py:
    Contiene funciones auxiliares a la vista, como el seteo de los widgets entry y,
    la construcción de la lista para movimiento de toda la información y la función
    de cierre de la aplicación.
"""

from tkinter.messagebox import askokcancel


# ***** MANIPULACION DE DATOS *****
class AuxVista:
    def __init__(
        self,
        var_dni,
        var_cuil,
        var_nombre,
        var_apellido,
        var_domicilio,
        var_fnacimiento,
        var_falta,
        var_art,
        var_obra,
        var_jornal,
        var_filtro,
        l_status,
        e_dni,
        e_cuil,
    ) -> None:
        """
        Constructor de la clase que recibe todas las variables necesarias
        para la operación de los modulos que componen esta clase.
        :param var_dni: El número de DNI
        :param var_cuil: El número de CUIL
        :param var_nombre: El nombre/s de la persona
        :param var_apellido: El apellido/s de la persona
        :param var_domicilio: El domicilio declarado
        :param var_fnacimiento: La fecha de nacimiento
        :param var_falta: La fecha de alta en el sistema o la empresa
        :param var_art: Cual es la compañia de seguro o ART
        :param var_obra: La obra a la cual fue asignado/a
        :param var_jornal: El valor del jornal diario
        :param var_filtro: El dato para el filtrado por obra en el treeview
        :param l_status: Objeto label para mostrar la información
        :param e_dni: Objeto entry para bloquear o desbloquear el campo DNI
        :param e_cuil: Objeto entry para bloquear o desbloquear el campo CUIL
        """
        self.var_dni = var_dni
        self.var_cuil = var_cuil
        self.var_nombre = var_nombre
        self.var_apellido = var_apellido
        self.var_domicilio = var_domicilio
        self.var_fnacimiento = var_fnacimiento
        self.var_falta = var_falta
        self.var_art = var_art
        self.var_obra = var_obra
        self.var_jornal = var_jornal
        self.var_filtro = var_filtro
        self.l_status = l_status
        self.e_dni = e_dni
        self.e_cuil = e_cuil

    # ----- CREACION DE UNA LISTA PARA MOVIMIENTO DE LOS DATOS -----
    def create_list(self) -> list:
        """
        Se crea una lista con todos los datos del formulario para una más simple manipulación de la información.
        :returns data_list: La lista con toda la información.
        :rtype: list[str, int]
        """
        data_list = [
            self.var_dni.get(),
            self.var_cuil.get(),
            self.var_nombre.get(),
            self.var_apellido.get(),
            self.var_domicilio.get(),
            self.var_fnacimiento.get(),
            self.var_falta.get(),
            self.var_obra.get().capitalize(),
            self.var_art.get(),
            self.var_jornal.get(),
        ]
        return data_list

    # ----- SETEO DE LOS ENTRY -----
    def set_entry(self, data_list: list) -> None:
        """
        Esta función se utiliza para la carga de la información, seleccionada en el treeview o consultada por la búsqueda,
        en todo los entry del frame de datos. En esta situación se deshabilitan los campos de DNI y CUIL que no pueden ser modificados.
        También se le puede enviar una lista vacia para poder limpiar todos los campos y en esta ocasión se habilitan los entry bloqueados.

        :param data_list: La lista con toda la información a cargar o vacia para limpiar
        """

        self.var_dni.set(data_list[0][1])
        self.var_cuil.set(data_list[0][2])
        self.var_nombre.set(data_list[0][3])
        self.var_apellido.set(data_list[0][4])
        self.var_domicilio.set(data_list[0][5])
        self.var_fnacimiento.set(data_list[0][6])
        self.var_falta.set(data_list[0][7])
        self.var_obra.set(data_list[0][8])
        self.var_art.set(data_list[0][9])
        self.var_jornal.set(data_list[0][10])
        if not data_list[0][1]:
            self.l_status.config(text="Ok.", background="#B9F582")
            self.e_dni.config(state="normal")
            self.e_cuil.config(state="normal")
        else:
            self.l_status.config(
                text="Puede modificar o dar de baja al registro.",
                background="#B9F582",
            )
            self.e_dni.config(state="disabled")
            self.e_cuil.config(state="disabled")

    # ----- FUNCION DE CIERRE DE LA APLICACION -----
    def close_app(self, window) -> None:
        """
        Función para el cierre de la aplicación, con una ventana emergente que consulta si está seguro de esta operación.

        :param window: Objeto de tkinter, la ventana principal
        """
        option = askokcancel("Cerrar la aplicación", "¿Está seguro que quiere salir?")
        if option:
            window.destroy()
