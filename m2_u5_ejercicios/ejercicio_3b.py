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
    def __init__(self, color, matricula, velocidad, peso):
        super(Trenes, self).__init__(color, matricula, velocidad)
        self.peso = peso

    def imprimir(self):

        print(
            f"Color: {self.color} Matricula: {self.matricula} Velocidad maxima: {self.velocidad} Km/h Peso: {self.peso} t"
        )


print("\n", "- autos -" * 5)
auto1 = Vehiculos("rojo", "ABC 123", 130)
auto2 = Vehiculos("azul", "JGH 456", 145)
auto3 = Vehiculos("negro", "XYZ 567", 160)

auto1.imprimir()
auto2.imprimir()
auto3.imprimir()

print("\n", "- trenes -" * 5)
tren1 = Trenes("amarillo", "13 OH", 180, 3.5)
tren2 = Trenes("marron", "45 ZX", 170, 4.5)

tren1.imprimir()
tren2.imprimir()

# autos = [
#     Vehiculos("rojo", "ABC 123", 130),
#     Vehiculos("azul", "JGH 456", 145),
#     Vehiculos("negro", "XYZ 567", 160),
# ]
# trenes = [Trenes("amarillo", "13 OH", 180, 3.5), Trenes("marron", "45 ZX", 170, 4.5)]

# print("\n", "- autos -" * 5)
# for auto in autos:
#     auto.imprimir()

# print("\n", "- trenes -" * 5)
# for tren in trenes:
#     tren.imprimir()
