class Vehiculos:
    def __init__(self, color, matricula, velocidad):
        self.color = color
        self.matricula = matricula
        self.velocidad = velocidad

    def imprimir(self):

        print(
            f"Color: {self.color} Matricula: {self.matricula} Velocidad maxima: {self.velocidad} Km/h"
        )


auto1 = Vehiculos("rojo", "ABC 123", 130)
auto2 = Vehiculos("azul", "JGH 456", 145)
auto3 = Vehiculos("negro", "XYZ 567", 160)

auto1.imprimir()
auto2.imprimir()
auto3.imprimir()
