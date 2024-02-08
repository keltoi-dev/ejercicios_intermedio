class Vehiculos:
    def __init__(self, color, matricula, velocidad):
        self.color = color
        self.matricula = matricula
        self.velocidad = velocidad


auto1 = Vehiculos("rojo", "ABC 123", 130)
auto2 = Vehiculos("azul", "JGH 456", 145)
auto3 = Vehiculos("negro", "XYZ 567", 160)

print(
    f"Color: {auto1.color} Matricula: {auto1.matricula} Velocidad maxima: {auto1.velocidad} Km/h"
)
print(
    f"Color: {auto2.color} Matricula: {auto2.matricula} Velocidad maxima: {auto2.velocidad} Km/h"
)
print(
    f"Color: {auto3.color} Matricula: {auto3.matricula} Velocidad maxima: {auto3.velocidad} Km/h"
)
