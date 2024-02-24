# Practicando POO
# Germán Fraga
import re
import os


class RegexError(Exception):

    BASE_DIR = os.getcwd() + os.sep
    ruta = BASE_DIR + "log.txt"

    def __init__(self, detalle):
        self.detalle = detalle

    def guardar_error(self):
        log_errors = open(self.ruta, "a")
        print("Se ingreso mal el dato en", self.detalle, file=log_errors)


class RegexCampos:
    def __init__(self, codigo: str, data: str, funcion: str):
        self.codigo = codigo
        self.data = data
        self.funcion = funcion

    def verificar(self):
        if not re.match(self.codigo, self.data):
            raise RegexError(self.funcion)
