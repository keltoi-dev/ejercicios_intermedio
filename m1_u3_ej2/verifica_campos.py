# Practicando POO
# Germán Fraga
import re


class RegexCampos:
    def __init__(self) -> None:
        pass

    def verificar(self, codigo: str, data: str) -> bool:
        return re.match(codigo, data)
