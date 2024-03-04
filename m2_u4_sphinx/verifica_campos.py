"""
verifica_campos.py:
    Verificacion de datos con un regex especifico.
"""

import re
import os
import datetime


class RegexError(Exception):
    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "log.txt")

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

    def __init__(self, codigo: str, data: str, funcion: str) -> None:
        self.codigo = codigo
        self.data = data
        self.funcion = funcion

    def verificar(self) -> None:
        """
        Función que controla el cumplimiento de los parámetros enviados en la instancia y
        en caso de no concordancia genera un raise.

        :raises: RegexError
        """
        if not re.match(self.codigo, self.data):
            raise RegexError(self.funcion)
