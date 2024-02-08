class Vehiculos:
    def __init__(self, color, matricula, velocidad):
        self.color = color
        self.matricula = matricula
        self.velocidad = velocidad

    def imprimir(self):

        print(
            f"Color: {self.color} Matricula: {self.matricula} Velocidad maxima: {self.velocidad} Km/h"
        )


class Trenes(Vehiculos):
    def __init__(self, color, matricula, velocidad):
        self.color = color
        self.matricula = matricula
        self.velocidad = velocidad


print("\n", "- autos -" * 5)
auto1 = Vehiculos("rojo", "ABC 123", 130)
auto2 = Vehiculos("azul", "JGH 456", 145)
auto3 = Vehiculos("negro", "XYZ 567", 160)

Vehiculos.imprimir(auto1)
Vehiculos.imprimir(auto2)
Vehiculos.imprimir(auto3)

print("\n", "- trenes -" * 5)
tren1 = Trenes("amarillo", "13 OH", 180)
tren2 = Trenes("marron", "45 ZX", 170)

Trenes.imprimir(tren1)
Trenes.imprimir(tren2)
