# Practicando POO
# Germán Fraga
import re
import os
import datetime


class RegexError(Exception):

    BASE_DIR = os.getcwd() + os.sep
    ruta = BASE_DIR + "log.txt"

    def __init__(self, detalle: str) -> None:
        self.detalle = detalle

    def guardar_error(self) -> None:
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
        if not re.match(self.codigo, self.data):
            raise RegexError(self.funcion)
