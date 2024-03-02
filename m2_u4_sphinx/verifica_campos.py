"""
verifica_campos.py:
    Verificacion de datos con un regex especifico.
"""

import re
import os
import datetime


class RegexError(Exception):
    """
    Clase para la generación de un propio tipo de error para el manejo de
    excepciones en el control del regex de los campos.
    Genera un un log con la información del error.
    """

    BASE_DIR = os.getcwd() + os.sep
    ruta = BASE_DIR + "log.txt"

    def __init__(self, detalle: str) -> None:
        self.detalle = detalle

    def guardar_error(self) -> None:
        """
        Función que guarda el tipo de error, donde se localizó y la fecha y hora.
        """
        log_errors = open(self.ruta, "a")
        print(
            datetime.datetime.now(),
            "- Se ingreso mal el dato en",
            self.detalle,
            file=log_errors,
        )


class RegexCampos:
    """
    Clase para el control de un regex y un dato.
    """

    def __init__(self, codigo: str, data: str, funcion: str) -> None:
        """
        Constructor de la clase.

        :param codigo: String con la clave del regex
        :param data: String con el dato a corroborar
        :param funcion: String con la ubicacion desde donde se instancia
        """
        self.codigo = codigo
        self.data = data
        self.funcion = funcion

    def verificar(self) -> None:
        """
        Función que controla el cumplimiento de los parámetros enviados en la instancia y
        en caso de no concordancia genera un raise.
        """
        if not re.match(self.codigo, self.data):
            raise RegexError(self.funcion)
